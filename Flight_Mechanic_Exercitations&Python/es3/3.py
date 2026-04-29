import numpy 
import matplotlib.pyplot as plt
from Func import p_rho_T
from Func import eval_aerodynamic_coefficients


CL_i, Cd_i, Cm_i = eval_aerodynamic_coefficients (alpha = 0.0, Re = '5e4', airfoil = 'NACA2412')

################################# Re=5e4 ###############################
"CL:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
CL_Re5e4 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '5e4', airfoil = 'NACA2412')
    CL_Re5e4[i] = CL_i
 
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, CL_Re5e4, color='r', marker='.')
ax.set_title("CL_Re5e4 vs Alpha")
plt.xlabel('Alpha')
plt.ylabel('Cl')
ax.axhline(0, color='black', linestyle='--')
ax.axvline(0, color='black', linestyle='--')
plt.show()  


"CM:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
Cm_Re5e4 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '5e4', airfoil = 'NACA2412')
    Cm_Re5e4[i] = Cm_i
 
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, Cm_Re5e4,color='g', marker='.')
plt.xlabel('Alpha')
plt.ylabel('Cm 5e4')
plt.show()



"CD:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
Cd_Re5e4 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '5e4', airfoil = 'NACA2412')
    Cd_Re5e4[i] = Cd_i
 
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, Cd_Re5e4,color='b', marker='.')
plt.xlabel('Alpha')
plt.ylabel('Cd 5e4')
plt.show()

"POLARE:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
Cd_Re5e4 = numpy.zeros_like(alpha)
CL_Re5e4 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '5e4', airfoil = 'NACA2412')
    Cd_Re5e4[i] = Cd_i
    CL_Re5e4[i] = CL_i
    
 
fig = plt.figure()
ax = fig.gca()
ax.plot(CL_Re5e4, Cd_Re5e4, color='purple', marker='.')
plt.xlabel('CL 5e4')
plt.ylabel('Cd 5e4')
plt.show()

################################# Re=2e5 ###############################
"CL:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
CL_Re2e5 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '2e5', airfoil = 'NACA2412')
    CL_Re2e5[i] = CL_i
 
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, CL_Re2e5,color='r', marker='.')
plt.xlabel('Alpha')
plt.ylabel('Cl 2e5')
plt.show()  


"CM:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
Cm_Re2e5 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '2e5', airfoil = 'NACA2412')
    Cm_Re2e5[i] = Cm_i
 
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, Cm_Re2e5,color='g', marker='.')
plt.xlabel('Alpha')
plt.ylabel('Cm 2e5')
plt.show()



"CD:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
Cd_Re2e5 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '2e5', airfoil = 'NACA2412')
    Cd_Re2e5[i] = Cd_i
 
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, Cd_Re2e5,color='b', marker='.')
plt.xlabel('Alpha')
plt.ylabel('Cd 2e5')
plt.show()

"POLARE:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
Cd_Re2e5 = numpy.zeros_like(alpha)
CL_Re2e5 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '2e5', airfoil = 'NACA2412')
    Cd_Re2e5[i] = Cd_i
    CL_Re2e5[i] = CL_i
    
fig = plt.figure()
ax = fig.gca()
ax.plot(CL_Re5e4, Cd_Re5e4, color='purple', marker='.')     
plt.xlabel('CL 2e5')
plt.ylabel('Cd 2e5')
plt.show()

################################# Re=1e6 ###############################
"CL:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
CL_Re1e6 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cd_i, Cm_i = eval_aerodynamic_coefficients (alpha[i], Re = '1e6', airfoil = 'NACA2412')
    CL_Re1e6[i] = CL_i
 
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, CL_Re1e6,color='r', marker='.')
plt.xlabel('Alpha')
plt.ylabel('Cl 1e6')
plt.show()  


"CM:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
Cm_Re1e6 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '1e6', airfoil = 'NACA2412')
    Cm_Re1e6[i] = Cm_i
 
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, Cm_Re1e6,color='g', marker='.')
plt.xlabel('Alpha')
plt.ylabel('Cm 1e6')
plt.show()



"CD:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
Cd_Re1e6 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '1e6', airfoil = 'NACA2412')
    Cd_Re1e6[i] = Cd_i
 
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, Cd_Re1e6,color='b', marker='.')
plt.xlabel('Alpha')
plt.ylabel('Cd 1e6')
plt.show()

"POLARE:"
n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)
Cd_Re1e6 = numpy.zeros_like(alpha)
CL_Re1e6 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '1e6', airfoil = 'NACA2412')
    Cd_Re1e6[i] = Cd_i
    CL_Re1e6[i] = CL_i
    
 
fig = plt.figure()
ax = fig.gca()
ax.plot(CL_Re1e6, Cd_Re1e6, color='cyan', marker='.')
plt.xlabel('CL 1e6')
plt.ylabel('Cd 1e6')
plt.show()

################################################# PUNTO 4 ####################################

c = 1.3
pho_sl = 1.225
mi_sl = 1.789e-5

Re1 = 5e4
Re2 = 2e5
Re3 = 1e6

n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)

V1 = (Re1*mi_sl)/(pho_sl*c)
V2 = (Re2*mi_sl)/(pho_sl*c)
V3 = (Re3*mi_sl)/(pho_sl*c)
##########################################################################################
l1 = (1/2)*pho_sl*V1*V1*c*CL_Re5e4
l2 = (1/2)*pho_sl*V2*V2*c*CL_Re2e5
l3 = (1/2)*pho_sl*V3*V3*c*CL_Re1e6

"PLOT: l"

"l1"
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, l1, color='r', marker='.', label = 'Re_5e4')
plt.xlabel('alpha')
plt.ylabel('l_5e4')
plt.show()
"l2"
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, l2, color='cyan', marker='.', label = 'Re_2e5')
plt.xlabel('alpha')
plt.ylabel('l_2e5')
plt.show()
"l3"
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, l3, color='brown', marker='.', label = 'Re_1e6')
plt.xlabel('alpha')
plt.ylabel('l_1e6')
plt.show()

########################################################################################
d1 = (1/2)*pho_sl*V1*V1*c*Cd_Re5e4
d2 = (1/2)*pho_sl*V2*V2*c*Cd_Re2e5
d3 = (1/2)*pho_sl*V3*V3*c*Cd_Re1e6

"PLOT: d"

"d1"
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, d1, color='r', marker='.', label = 'Re_5e4')
plt.xlabel('alpha')
plt.ylabel('m_5e4')
plt.show()
"d2"
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, d2, color='cyan', marker='.', label = 'Re_2e5')
plt.xlabel('alpha')
plt.ylabel('m_2e5')
plt.show()
"d3"
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, d3, color='brown', marker='.', label = 'Re_1e6')
plt.xlabel('alpha')
plt.ylabel('m_1e6')
plt.show()
############################################################################################
m1 = (1/2)*pho_sl*V1*V1*c*(c/4)*Cm_Re5e4
m2 = (1/2)*pho_sl*V2*V2*c*(c/4)*Cm_Re2e5
m3 = (1/2)*pho_sl*V3*V3*c*(c/4)*Cm_Re1e6

"PLOT: m"

"m1"
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, m1, color='r', marker='.', label = 'Re_5e4')
plt.xlabel('alpha')
plt.ylabel('d_5e4')
plt.show()
"m2"
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, m2, color='cyan', marker='.', label = 'Re_2e5')
plt.xlabel('alpha')
plt.ylabel('d_2e5')
plt.show()
"m3"
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, m3, color='brown', marker='.', label = 'Re_1e6')
plt.xlabel('alpha')
plt.ylabel('d_1e6')
plt.show()

##############################################################################

'  INTERPOLAZIONE PER ALPHA 0 5e5  '

Alpha_1 = -1.500
Cl_1 = 0.0062
Alpha_2 = -1.750
Cl_2 = -0.0143 

Alpha_0_5e5 = ((Alpha_1-Alpha_2)*(-Cl_2)/(Cl_1-Cl_2)) + Alpha_2
#print(Alpha_0_5e5)


'  INTERPOLAZIONE PER ALPHA 0 1e6'

Alpha_1 = -1.500
Cl_1 = 0.0088 
Alpha_2 = -1.750
Cl_2 = -0.0169  

Alpha_0_1e6 = ((Alpha_1-Alpha_2)*(-Cl_2)/(Cl_1-Cl_2)) + Alpha_2
#print(Alpha_0_1e6)

' POLARE NACA 65210 Re 1e6 '

n = 100
alpha = numpy.linspace(-8.0, 11.0, num = n)
Cd_Re1e6 = numpy.zeros_like(alpha)
CL_Re1e6 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '1e6', airfoil = 'NACA65210')
    Cd_Re1e6[i] = Cd_i
    CL_Re1e6[i] = CL_i
    
 
fig = plt.figure()
ax = fig.gca()
ax.plot(CL_Re1e6, Cd_Re1e6, color='yellow', marker='.')
plt.xlabel('CL NACA-65210 1e6')
plt.ylabel('Cd NACA-65210 1e6')
plt.show()

' POLARE NACA 65210 Re 5e5 '

n = 100
alpha = numpy.linspace(-8.0, 11.0, num = n)
Cd_Re5e5 = numpy.zeros_like(alpha)
CL_Re5e5 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '5e5', airfoil = 'NACA65210')
    Cd_Re5e5[i] = Cd_i
    CL_Re5e5[i] = CL_i
    
 
fig = plt.figure()
ax = fig.gca()
ax.plot(CL_Re5e5, Cd_Re5e5, color='pink', marker='.')
plt.xlabel('CL NACA-65210 5e5')
plt.ylabel('Cd NACA-65210 5e5')
plt.show()

#####################################################################

'alpha    CL'
'------ --------'              
'-1.750  -0.0209'
'-1.500   0.0067'


alpha_0 = -1.750 + ((0.0209)/(0.0067+0.0209))*(-1.500+1.750)
#print(alpha_0)

b = 37
S = 233
AR = (b**2)/S
e = 0.99

Cl_alpha = (0.0067+0.0209)/(-1.500+1.750)
#print(Cl_alpha)
CLw_alpha = ((Cl_alpha)/(1 + (57.3*Cl_alpha)/(numpy.pi*e*AR)))
#print(CLw_alpha)

"Cl:"
n = 100
alpha = numpy.linspace(-8.0, 11.5, num = n)
CL_Re1e6 = numpy.zeros_like(alpha)

for i in range(n):
    CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = '1e6', airfoil = 'NACA65210')
    CL_Re1e6[i] = CL_i
 
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, CL_Re1e6,color='r', marker='.')
plt.xlabel('Alpha')
plt.ylabel('Cl 1e6')
plt.show()  

"CLw:"
n = 100
alpha = numpy.linspace(-8.5, 11.0, num = n)
CLw_Re1e6 = numpy.zeros_like(alpha)

CLw_Re1e6 = CLw_alpha*(alpha-alpha_0)
 
fig = plt.figure()
ax = fig.gca()
ax.plot(alpha, CLw_Re1e6,color='r', marker='.')
plt.xlabel('Alpha')
plt.ylabel('CLw 1e6')
plt.show()  

"POLARE Ala Finita:"

CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (-1.5606, Re = '1e6', airfoil = 'NACA65210')
#print(Cd_i)

n = 100
alpha = numpy.linspace(-8.0, 11.0, num = n)
CLw_Re1e6 = numpy.zeros_like(alpha)
CDw_Re1e6 = numpy.zeros_like(alpha)

CLw_Re1e6 = CLw_alpha*(alpha-alpha_0)   
CDw_Re1e6 = 0.0064652 + (CLw_Re1e6**2)/(numpy.pi*AR*e)


fig = plt.figure()
ax = fig.gca()
ax.plot(CLw_Re1e6, CDw_Re1e6, color='pink', marker='.')
plt.xlabel('CLw 1e6')
plt.ylabel('Cdw 1e6')
plt.show()

"POLARE Ala Finita con fusoliera:"

n = 100
alpha = numpy.linspace(-8.0, 11.0, num = n)
CLwf_Re1e6 = numpy.zeros_like(alpha)
CDwf_Re1e6 = numpy.zeros_like(alpha)

CLwf_Re1e6 = CLw_alpha*(alpha-alpha_0)
CDwf_Re1e6 = 0.0163 + (CLwf_Re1e6**2)/(numpy.pi*AR*e)

fig = plt.figure()
ax = fig.gca()
ax.plot(CLwf_Re1e6, CDwf_Re1e6, color='green', marker='.')
plt.xlabel('CLwf 1e6')
plt.ylabel('Cdwf 1e6')
plt.show()

######################################################

fig = plt.figure()
ax = fig.gca()

ax.plot(CL_Re1e6, Cd_Re1e6, color='cyan', marker='.', label = 'polare profilo')
ax.plot(CLw_Re1e6, CDw_Re1e6, color='pink', marker='.', label = 'polare ala finita')
ax.plot(CLwf_Re1e6, CDwf_Re1e6, color='green', marker='.', label = 'polare ala + fusoliera')

plt.xlabel('CDwf 1e6')
plt.xlabel('CLwf 1e6')
ax.legend()
plt.show()


# CAMBIA REYNLODS #########################################################

" Cl RE5e5 "

Cl_alpha_5e5 = (0.0062+0.0143)/(-1.500+1.750)
#print(Cl_alpha)
CLw_alpha_5e5 = ((Cl_alpha_5e5)/(1 + (57.3*Cl_alpha)/(numpy.pi*e*AR)))
#print(CLw_alpha)

"POLARE Ala Finita 5e5 :"

CL_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (-1.5606, Re = '5e5', airfoil = 'NACA65210')
#print(Cd_i)

n = 100
alpha = numpy.linspace(-8.0, 11.0, num = n)
CLw_Re5e5 = numpy.zeros_like(alpha)
CDw_Re5e5 = numpy.zeros_like(alpha)

CLw_Re5e5 = CLw_alpha_5e5*(alpha-alpha_0)   
CDw_Re5e5 = 0.0064652 + (CLw_Re5e5**2)/(numpy.pi*AR*e)


fig = plt.figure()
ax = fig.gca()
ax.plot(CLw_Re5e5, CDw_Re5e5, color='pink', marker='.')
plt.xlabel('CLw 5e5')
plt.ylabel('Cdw 5e5')
plt.show()

"POLARE Ala Finita con fusoliera:"

n = 100
alpha = numpy.linspace(-8.0, 11.0, num = n)
CLwf_Re5e5 = numpy.zeros_like(alpha)
CDwf_Re5e5 = numpy.zeros_like(alpha)

CLwf_Re5e5 = CLw_alpha_5e5*(alpha-alpha_0)
CDwf_Re5e5 = 0.0163 + (CLwf_Re5e5**2)/(numpy.pi*AR*e)

fig = plt.figure()
ax = fig.gca()
ax.plot(CLwf_Re5e5, CDwf_Re5e5, color='green', marker='.')
plt.xlabel('CLwf 5e5')
plt.ylabel('Cdwf 5e5')
plt.show()

######################################################

fig = plt.figure()
ax = fig.gca()

ax.plot(CL_Re1e6, Cd_Re1e6, color='cyan', marker='.', label = 'polare profilo')
ax.plot(CLw_Re1e6, CDw_Re1e6, color='pink', marker='.', label = 'polare ala finita')
ax.plot(CLwf_Re1e6, CDwf_Re1e6, color='green', marker='.', label = 'polare ala + fusoliera')

plt.xlabel('CDwf 5e5')
plt.xlabel('CLwf 5e5')
ax.legend()
plt.show()

###################################################################

visc_0 = 1.716e-5
T0 = 273
S_mhu = 111
Cd_0 = 0.0163
W = 4581.282937
CD_h = []
h = numpy.linspace(0, 12871, 100)
H_tangenza = 12871

for i in range(0, len(h)):
    T, p, rho = p_rho_T(h[i])
    visc = visc_0 * (numpy.power((T / T0), (3 / 2)) * ((T0 + S_mhu) / (T + S_mhu)))
    Re = 6e6
    V = (Re * visc) / (rho * 11.27)
    CD = Cd_0 + ((2 * W) / (rho * S)**2) * (1 / (V**4))
    CD_h.append(CD)

plt.plot(CD_h, h, marker=".")
plt.xlabel('CD_ac')
plt.ylabel('h')
plt.title('Grafico CD_ac vs h')
plt.show()

# QUESTION 3 ##############################################################

VKTAS =  95.1722
T, p, rho = p_rho_T(0)
Re_root = rho*VKTAS*11.6738/visc_0
S_ref = 13.4617

' WINGS '

k = 1+0.07
Ff = 1.311
Fi = 1 

S_area_wing = 5.921356983
S_wet_wings = S_area_wing*2*k

c_root = 1.4874 
c_tip = 0.789432

Re_root = rho*VKTAS*c_root/visc_0
Re_tip = rho*VKTAS*c_tip/visc_0

x_trans_root = 0.45*c_root
x_trans_tip_top = 0.6*c_tip
x_trans_tip_bottom = 0.5*c_tip

x_0_root = c_root*(36.9*((x_trans_root/c_root)**0.625)*(1/Re_root)**0.375)
x_0_tip_top = c_tip*(36.9*((x_trans_tip_top/c_tip)**0.625)*(1/Re_tip)**0.375) 
x_0_tip_bottom = c_tip*(36.9*((x_trans_tip_bottom/c_tip)**0.625)*(1/Re_tip)**0.375)  
         
Cf_root = (0.074/(Re_root**(1/5)))*(1-((x_trans_root-x_0_root)/c_root))**0.8
Cf_tip_top = (0.074/(Re_tip**(1/5)))*(1-((x_trans_tip_top-x_0_tip_top)/c_tip))**0.8
Cf_tip_bottom = (0.074/(Re_tip**(1/5)))*(1-((x_trans_tip_bottom-x_0_tip_bottom)/c_tip))**0.8
Cf_tip = (Cf_tip_top + Cf_tip_bottom)/2
Cf_wing = (Cf_tip+Cf_root)/2

CD0_wings = 2*(Cf_wing)*(S_wet_wings/S_ref)*Ff*Fi

print("CD0 wings is equal to: " + str(CD0_wings))

'# HORIZONTAL TAIL #########################################################'

Fi_tail = 1.05

Ff_vert = 1.187
Ff_horizon = 1.203

k_tail = 1+0.05

S_vert = 1.51203507
S_horizon = 1.306807425

S_wet_tail_vert = (S_vert)*k
S_wet_tail_horizon = (S_horizon)*k

' HORIZON '

c_root_tail = 0.850392
c_tip_tail = 0.557784

Re_root_tail = rho*VKTAS*c_root_tail/visc_0
Re_tip_tail = rho*VKTAS*c_tip_tail/visc_0

x_trans_root_tail = 0.5*c_root_tail
x_trans_tip_tail = 0.5*c_tip_tail

x_0_root_tail = c_root_tail*(36.9*((x_trans_root_tail/c_root_tail)**0.625)*(1/Re_root_tail)**0.375)
x_0_tip_tail = c_tip_tail*(36.9*((x_trans_tip_tail/c_tip_tail)**0.625)*(1/Re_tip_tail)**0.375)

Cf_root_tail = (0.074/(Re_root_tail**(1/5)))*(1-((x_trans_root_tail-x_0_root_tail)/c_root_tail))**0.8
Cf_tip_tail = (0.074/(Re_tip_tail**(1/5)))*(1-((x_trans_tip_tail-x_0_tip_tail)/c_tip_tail))**0.8

l = (Cf_root_tail + Cf_tip_tail )/2

' VERTICAL '

c_root_tailv = 1.2436
c_tip_tailv = 0.62484

Re_tip_tailv = rho*VKTAS*c_tip_tailv/visc_0
Re_root_tailv = rho*VKTAS*c_root_tailv/visc_0

x_trans_root_tailv = 0.5*c_root_tailv
x_trans_tip_tailv = 0.5*c_tip_tailv

x_0_root_tailv = c_root_tailv*(36.9*((x_trans_root_tailv/c_root_tailv)**0.625)*(1/Re_root_tailv)**0.375)
x_0_tip_tailv = c_tip_tailv*(36.9*((x_trans_tip_tailv/c_tip_tailv)**0.625)*(1/Re_tip_tailv)**0.375)

Cf_root_tailv = (0.074/(Re_root_tailv**(1/5)))*(1-((x_trans_root_tailv-x_0_root_tailv)/c_root_tailv))**0.8
Cf_tip_tailv = (0.074/(Re_tip_tailv**(1/5)))*(1-((x_trans_tip_tailv-x_0_tip_tailv)/c_tip_tailv))**0.8
    
m = (Cf_root_tailv + Cf_tip_tailv )/2

' CD0 TAIL '

CD0_tail = ((2*l)*(S_wet_tail_horizon)*Ff_horizon + (m)*(S_wet_tail_vert)*Ff_vert)*(Fi_tail/S_ref)
print("CD0_tail is equal to: " + str(CD0_tail))

' FUSELAGE '

S_wet_fuselage = 23.9318

Fi_fuselage = 1.399
Ff_fuselage = 1

c_fuselage = 6.8336
Re_fuselage = rho*VKTAS*c_fuselage/visc_0

x_trans_fuselage = 0.05*c_fuselage
x_0_fuselage = c_fuselage*(36.9*((x_trans_fuselage/c_fuselage)**0.625)*(1/Re_fuselage)**0.375)

Cf_fuselage = (0.074/(Re_fuselage**(1/5)))*(1-((x_trans_fuselage-x_0_fuselage)/c_fuselage))**0.8

CD0_fuselage = (Cf_fuselage)*(S_wet_fuselage/S_ref)*Ff_fuselage*Fi_fuselage
print("CD0_fusalage is equal to: " + str(CD0_fuselage))

CD0_Tot = CD0_fuselage + CD0_tail + CD0_wings
print("CD0_tot is equal to: " + str(CD0_Tot)) 
