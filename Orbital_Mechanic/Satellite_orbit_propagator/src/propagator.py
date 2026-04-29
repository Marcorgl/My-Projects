"""
Orbital Mechanics Propagator
Simulates satellite orbits with perturbations (J2, atmospheric drag)
Uses scipy.integrate for numerical ODE solving
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation

# ============================================================================
# PHYSICAL CONSTANTS
# ============================================================================

MU = 3.986004418e14  # Earth gravitational parameter (m³/s²)
R_E = 6.371e6  # Earth radius (m)
J2 = 1.081874e-3  # J2 coefficient (dimensionless) - Earth oblateness

# Atmospheric model constants (exponential density profile)
rho_0 = 1.225  # Air density at sea level (kg/m³)
H = 8500  # Scale height (m)

# Drag model constants (8U CubeSat parameters)
DRAG_CD = 2.2  # Drag coefficient (dimensionless)
DRAG_A = 0.04  # Frontal area (m²) - 0.2m × 0.2m
DRAG_M = 15  # Satellite mass (kg)


# ============================================================================
# ACCELERATION FUNCTIONS
# ============================================================================


def acceleration_gravity(position):
    """
    Calculate gravitational acceleration from central body.
    Uses point mass assumption (valid for r >> Earth radius)

    Args:
        position: [x, y, z] position vector in meters

    Returns:
        acceleration: [ax, ay, az] acceleration vector in m/s²
    """
    r = np.linalg.norm(position)  # Distance from Earth center
    coeff = -MU / (r**3)  # Gravitational coefficient
    acceleration = coeff * position  # F = -μ/r³ * r_vec

    return acceleration


def acceleration_j2(position):
    """
    Calculate J2 perturbation acceleration due to Earth's oblateness.
    J2 is the dominant perturbation for most LEO satellites.
    Causes orbital precession and oscillations.

    Args:
        position: [x, y, z] position vector in meters

    Returns:
        a_j2: [ax, ay, az] J2 perturbation acceleration in m/s²
    """
    r = np.linalg.norm(position)

    # J2 perturbation coefficient: (3/2) * J2 * μ * R_E² / r⁵
    coeff = (3 / 2) * J2 * MU * (R_E**2) / (r**5)

    # Extract z-component for J2 calculation
    z = position[2]

    # Common factor for X and Y components
    factor = 5 * (z / r) ** 2 - 1

    # Build perturbation acceleration vector
    vector = np.array(
        [
            factor * position[0],  # X component
            factor * position[1],  # Y component
            (5 * (z / r) ** 2 - 3) * position[2],  # Z component (different)
        ]
    )

    a_j2 = coeff * vector

    return a_j2


def atmospheric_density(altitude):
    """
    Calculate atmospheric density using exponential model.
    Density decreases exponentially with altitude.

    Args:
        altitude: height above Earth surface (m)

    Returns:
        rho: atmospheric density (kg/m³)
    """
    rho = rho_0 * np.exp(-altitude / H)
    return rho


def acceleration_drag(position, velocity):
    """
    Calculate atmospheric drag acceleration.
    Drag opposes motion and is significant only at low altitudes (<300 km).

    Args:
        position: [x, y, z] position vector in meters
        velocity: [vx, vy, vz] velocity vector in m/s

    Returns:
        a_drag: [ax, ay, az] drag acceleration in m/s²
    """
    r = np.linalg.norm(position)
    altitude = r - R_E  # Height above surface

    rho = atmospheric_density(altitude)  # Get density at altitude
    v_mag = np.linalg.norm(velocity)  # Velocity magnitude

    # Drag acceleration coefficient: -1/2 * ρ * v * C_d * A / m
    coeff = -0.5 * rho * v_mag * DRAG_CD * DRAG_A / DRAG_M

    # Drag opposes velocity direction
    a_drag = coeff * velocity

    return a_drag


# ============================================================================
# ODE SYSTEM AND PROPAGATOR
# ============================================================================


def equations_of_motion(t, state, include_j2=True, include_drag=True):
    """
    Define the system of ODEs for satellite motion.
    Converts 2nd-order equations to 1st-order system.

    State vector: [x, y, z, vx, vy, vz]
    dr/dt = v
    dv/dt = a_total (sum of all accelerations)

    Args:
        t: time (seconds) - required by solve_ivp but not used
        state: [x, y, z, vx, vy, vz] position and velocity
        include_j2: whether to include J2 perturbation
        include_drag: whether to include atmospheric drag

    Returns:
        derivatives: [vx, vy, vz, ax, ay, az]
    """
    position = state[:3]  # Extract position [x, y, z]
    velocity = state[3:]  # Extract velocity [vx, vy, vz]

    # Start with gravitational acceleration (always included)
    acceleration = acceleration_gravity(position)

    # Add perturbations if enabled
    if include_j2:
        acceleration += acceleration_j2(position)

    if include_drag:
        acceleration += acceleration_drag(position, velocity)

    # Concatenate position derivatives (velocity) and velocity derivatives (acceleration)
    derivatives = np.concatenate([velocity, acceleration])

    return derivatives


def propagate_orbit(
    position_0, velocity_0, time_span, include_j2=True, include_drag=True, n_points=1000
):
    """
    Propagate satellite orbit using numerical ODE solver.
    Uses scipy.integrate.solve_ivp with RK45 method.

    Args:
        position_0: [x, y, z] initial position (m)
        velocity_0: [vx, vy, vz] initial velocity (m/s)
        time_span: (t_start, t_end) integration time (seconds)
        include_j2: include J2 perturbation?
        include_drag: include atmospheric drag?
        n_points: number of output points

    Returns:
        sol: scipy solution object with .t and .y attributes
    """
    # Combine position and velocity into state vector
    state_0 = np.concatenate([position_0, velocity_0])

    # Create array of time points where solution will be evaluated
    t_eval = np.linspace(time_span[0], time_span[1], n_points)

    # Solve the ODE system
    sol = solve_ivp(
        equations_of_motion,
        time_span,
        state_0,
        t_eval=t_eval,
        method="RK45",  # Runge-Kutta 4/5 adaptive step
        max_step=10,  # Maximum time step (seconds)
        args=(include_j2, include_drag),  # Pass perturbation flags
    )

    return sol


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # ========================================================================
    # INITIAL CONDITIONS
    # ========================================================================

    # Orbit parameters
    h_altitude = 500e3  # 500 km altitude
    r_orbit = R_E + h_altitude  # Orbital radius from Earth center
    position_0 = np.array([r_orbit, 0, 0])  # Start on equator, X-axis

    # Circular orbit velocity (Keplerian, no perturbations)
    velocity_0 = np.array([0, np.sqrt(MU / r_orbit), 0])

    # Compute orbital period using Kepler's 3rd law: T = 2π√(a³/μ)
    N_ORBITS = 1
    T = 2 * np.pi * np.sqrt(r_orbit**3 / MU)
    time_span = (0, N_ORBITS * T)
    n_points = N_ORBITS * 500  # 500 points per orbit for smooth resolution

    print(f"Orbital period: {T/60:.2f} minutes")
    print(f"Simulating {N_ORBITS} orbit(s) for {N_ORBITS * T / 60:.2f} minutes\n")

    # ========================================================================
    # PROPAGATIONS
    # ========================================================================

    # Keplerian propagation (gravity only - idealized)
    print(f"Propagating Keplerian orbit (gravity only)...")
    sol_kepler = propagate_orbit(
        position_0,
        velocity_0,
        time_span,
        include_j2=False,
        include_drag=False,
        n_points=n_points,
    )

    # Full propagation (gravity + J2 + drag - realistic)
    print(f"Propagating full orbit (gravity + J2 + drag)...")
    sol_full = propagate_orbit(
        position_0,
        velocity_0,
        time_span,
        include_j2=True,
        include_drag=True,
        n_points=n_points,
    )

    print("Propagation complete.\n")

    # ========================================================================
    # EXTRACT RESULTS
    # ========================================================================

    # Extract time and position from solution objects
    t_kepler = sol_kepler.t
    r_kepler = sol_kepler.y[:3].T  # Shape: [N points, 3]

    t_full = sol_full.t
    r_full = sol_full.y[:3].T  # Shape: [N points, 3]

    # Calculate altitude (distance from surface, not center)
    h_kepler = np.linalg.norm(r_kepler, axis=1) - R_E
    h_full = np.linalg.norm(r_full, axis=1) - R_E

    # ========================================================================
    # PLOT 1: STATIC COMPARISON PLOTS
    # ========================================================================

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left plot: Altitude vs Time
    ax = axes[0]
    ax.plot(
        t_kepler / 60,
        h_kepler / 1e3,
        "b-",
        label="Keplerian (gravity only)",
        linewidth=2,
    )
    ax.plot(
        t_full / 60, h_full / 1e3, "r-", label="Full (gravity + J2 + drag)", linewidth=2
    )
    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Altitude (km)")
    ax.set_title(f"Altitude vs Time ({N_ORBITS} orbit)")
    ax.grid(True, alpha=0.3)
    ax.legend()

    # Right plot: Orbital trace in XY plane
    ax = axes[1]
    ax.plot(
        r_kepler[:, 0] / 1e6, r_kepler[:, 1] / 1e6, "b-", label="Keplerian", linewidth=2
    )
    ax.plot(r_full[:, 0] / 1e6, r_full[:, 1] / 1e6, "r-", label="Full", linewidth=2)

    # Load and display Earth image
    from PIL import Image
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox

    earth_path = r"C:\Users\Marco\Desktop\marco\Git\My-Projects\Orbital_Mechanic\notebooks\earth.png"
    earth_img = Image.open(earth_path)
    earth_offset = OffsetImage(earth_img, zoom=0.25)
    earth_box = AnnotationBbox(earth_offset, (0, 0), frameon=False)
    ax.add_artist(earth_box)

    ax.set_xlabel("X (Mm)")
    ax.set_ylabel("Y (Mm)")
    ax.set_title(f"Orbital Trace XY plane ({N_ORBITS} orbit)")
    ax.axis("equal")
    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()
    plt.savefig("orbit_comparison.png", dpi=150)
    print("Static plots saved as 'orbit_comparison.png'\n")
    plt.show()

    # ========================================================================
    # PLOT 2: ANIMATED ORBIT
    # ========================================================================

print("Creating animation...")

fig_anim, ax_anim = plt.subplots(figsize=(10, 10))

# Load Earth image (optional - uncomment if you have the PNG)
from PIL import Image

earth_path = (
    r"C:\Users\Marco\Desktop\marco\Git\My-Projects\Orbital_Mechanic\notebooks\earth.png"
)
try:
    earth_img = Image.open(earth_path)
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox

    earth_offset = OffsetImage(earth_img, zoom=0.3)
    earth_box = AnnotationBbox(earth_offset, (0, 0), frameon=False)
    ax_anim.add_artist(earth_box)
except FileNotFoundError:
    # Fallback: draw Earth as circle if PNG not found
    earth = plt.Circle((0, 0), R_E / 1e6, color="green", alpha=0.3, label="Earth")
    ax_anim.add_patch(earth)


# Set plot limits and aspect
ax_anim.set_xlim(-10, 10)
ax_anim.set_ylim(-10, 10)
ax_anim.set_aspect("equal")
ax_anim.grid(True, alpha=0.3)
ax_anim.set_xlabel("X (Mm)")
ax_anim.set_ylabel("Y (Mm)")
ax_anim.set_title("Orbital Animation (Full: gravity + J2 + drag)")

# Initialize satellite as scatter point
satellite_scatter = ax_anim.scatter(
    [], [], s=100, c="red", marker="o", label="Satellite"
)

# Initialize trail (orbit path behind satellite)
(trail,) = ax_anim.plot([], [], "r-", linewidth=1, alpha=0.5, label="Trail")

ax_anim.legend()

# Animation parameters
TRAIL_LENGTH = 100  # Number of points to show in trail


def update(frame):
    """Update function called for each animation frame."""
    # Current satellite position (convert to Mm for plotting)
    x = r_full[frame, 0] / 1e6
    y = r_full[frame, 1] / 1e6

    # Update satellite position
    satellite_scatter.set_offsets([[x, y]])

    # Update trail: show last TRAIL_LENGTH points
    start = max(0, frame - TRAIL_LENGTH)
    trail_x = r_full[start:frame, 0] / 1e6
    trail_y = r_full[start:frame, 1] / 1e6
    trail.set_data(trail_x, trail_y)

    return satellite_scatter, trail


# Create animation
anim = FuncAnimation(fig_anim, update, frames=len(r_full), interval=20, blit=True)

anim.save("orbital_animation.gif", writer="pillow")

plt.tight_layout()
print("Animation running...\n")
plt.show()

print("Complete!")
