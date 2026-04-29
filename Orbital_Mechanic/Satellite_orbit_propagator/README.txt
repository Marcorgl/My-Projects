# Satellite Orbit Propagator

An orbital mechanics simulator that models satellite trajectories in Low Earth Orbit (LEO) with realistic perturbations.

## Overview

This project simulates the motion of satellites around Earth using numerical integration of orbital equations of motion. It compares Keplerian orbits with a semi-realistic orbits that include J2 perturbation and atmospheric drag effects.

**Key Features:**
- Numerical ODE solver (scipy RK45 method)
- Gravitational acceleration (2-body problem)
- J2 perturbation (Earth oblateness)
- Atmospheric drag modeling
- Real-time orbital animation
- Static comparison plots

## Physics Background

### Equations of Motion

The satellite motion is governed by Newton's second law in the Earth-centered inertial frame:

```
d²r/dt² = -μ/r³ * r + a_J2 + a_drag
```

Where:
- r = position vector [x, y, z]
- μ = Earth's gravitational parameter (3.986 × 10¹⁴ m³/s²)
- a_J2 = J2 perturbation acceleration
- a_drag = atmospheric drag acceleration

### J2 Perturbation

Earth is not a perfect sphere, it is oblate (flattened at the poles). This causes the J2 perturbation, which:
- Causes orbital precession
- Creates oscillations in orbital elements
- Is the dominant perturbation for LEO satellites

Magnitude: ~1000 times smaller than gravity but still significant over many orbits.

### Atmospheric Drag

At low altitudes, residual atmosphere causes drag proportional to:

```
a_drag = -1/2 * ρ * v * C_d * A / m
```

Where ρ decreases exponentially with altitude. At 500 km, drag is negligible (~10⁻²¹ m/s²) but becomes critical below 300 km.


### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/satellite_orbit_propagator.git
cd satellite_orbit_propagator
```

2. **Install dependencies:**
```bash
pip install numpy scipy matplotlib pillow
```

## Usage

### Run the simulation:

```bash
cd src
python propagator.py
```

This will:
1. Propagate a 500 km altitude circular orbit for 1 complete revolution (~94 minutes)
2. Compare Keplerian (gravity only) vs Full (gravity + J2 + drag) propagation
3. Display:
   - **Altitude vs Time plot**: Shows J2-induced oscillations
   - **Orbital Trace plot**: 2D projection with Earth image/circle
   - **Animated orbit**: Real-time satellite motion with trail

### Customize parameters:

Edit `src/propagator.py` in the `if __name__ == "__main__":` section:

```python
h_altitude = 500e3          # Change altitude (m)
N_ORBITS = 1                # Change number of orbits to simulate
DRAG_A = 0.04               # Change frontal area (m²)
DRAG_M = 15                 # Change satellite mass (kg)
```

## Results Interpretation

**Why the oscillation?**
The Keplerian velocity is calculated without J2. When J2 is added, the satellite is no longer in perfect equilibrium, causing the orbit to become slightly elliptical with periapsis (~480 km) and apoapsis (~500 km).


## Technical Details

### Orbital Elements

Initial conditions for 500 km altitude:
- Semiaxis: a = 6,871 km
- Eccentricity: e = 0 (circular)
- Inclination: i = 0° (equatorial)
- Period: T ≈ 94.5 minutes

### Constants

All constants follow NASA/ESA standards:

| Parameter | Value | Source |
|-----------|-------|--------|
| Earth μ | 3.986 × 10¹⁴ m³/s² | WGS84 |
| Earth radius | 6.371 × 10⁶ m | WGS84 |
| J2 coefficient | 1.081874 × 10⁻³ | IERS |
| Scale height | 8,500 m | Standard atmosphere |


## Future Extensions

Possible improvements:

- [ ] Add more perturbations (J3, J4, lunisolar)
- [ ] Implement station-keeping maneuvers
- [ ] 3D visualization with interactive controls
- [ ] Implement Orekit bindings for higher fidelity
- [ ] Monte Carlo uncertainty analysis

## References

**Textbooks:**
- Bate, Mueller, White. *Fundamentals of Astrodynamics* (1971)
- Vallado, Crawford, Hujsa, Johnston. *Celestial Mechanics and Astrodynamics*

**Standards:**
- IERS Conventions (for gravitational parameters)
- WGS84 (for Earth parameters)
- NASA SP-8013 (for atmospheric models)
