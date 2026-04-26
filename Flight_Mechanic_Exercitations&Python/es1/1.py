# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:58:26 2023

@author: 39348
"""

import math
import scipy
import numpy 
from matplotlib import pyplot as plt
import sys
import scipy.optimize

# DATA ############################################################

g = 9.81
R_air = 287.07 
rho_0 = 1.225
p_0 = 101325.0

# VETTORI DI BASE##################################################

C1 = -6.5e-3
C2 = 3e-3
C3 = -4.5e-3
C4 = 4e-3

altitude = numpy.array([0.0, 11e3, 25e3, 47e3, 53e3, 79e3, 90e3, 105e3])
temperature = numpy.array([288.16, 216.66, 216.66, 282.66, 282.66, 165.66, 165.66, 225.66])
pressure = numpy.zeros_like(altitude)
density = numpy.zeros_like(altitude)

# ELEMENTS PRESSURE #############################################
pressure[0] = p_0
pressure[1] = pressure[0]*(temperature[1]/temperature[0])**((-g)/(R_air*C1))
pressure[2] = pressure[1]*numpy.exp((-g*(altitude[2]-altitude[1]))/(R_air*temperature[2]))
pressure[3] = pressure[2]*(temperature[3]/temperature[2])**((-g)/(R_air*C2))
pressure[4] = pressure[3]*numpy.exp((-g*(altitude[4]-altitude[3]))/(R_air*temperature[4]))
pressure[5] = pressure[4]*(temperature[5]/temperature[4])**((-g)/(R_air*C3))
pressure[6] = pressure[5]*numpy.exp((-g*(altitude[6]-altitude[5]))/(R_air*temperature[6]))
pressure[7] = pressure[6]*(temperature[7]/temperature[6])**((-g)/(R_air*C4))

# ELEMENTS DENSITY #############################################
density[0] = rho_0
density[1] = density[0]*(temperature[1]/temperature[0])**((-g)/(R_air*C1)-1)
density[2] = density[1]*numpy.exp((-g*(altitude[2]-altitude[1]))/(R_air*temperature[2]))
density[3] = density[2]*(temperature[3]/temperature[2])**((-g)/(R_air*C2)-1)
density[4] = density[3]*numpy.exp((-g*(altitude[4]-altitude[3]))/(R_air*temperature[4]))
density[5] = density[4]*(temperature[5]/temperature[4])**((-g)/(R_air*C3)-1)
density[6] = density[5]*numpy.exp((-g*(altitude[6]-altitude[5]))/(R_air*temperature[6]))
density[7] = density[6]*(temperature[7]/temperature[6])**((-g)/(R_air*C4)-1)

# FUNCTION #####################################################

def p_rho_T(h_input, h_flag = "hG"):
    
    if (h_flag == "hG"):
         rE = 6378.0e3
         h = rE*h_input/(rE+h_input)
    else:
        h = h_input
        
    if h >= altitude[0] and h < altitude[1]:
        T = temperature[0]+C1*(h-altitude[0])
        p = pressure[0]*(T/temperature[0])**((-g)/(R_air*C1))
        rho = density[0]*(T/temperature[0])**((-g)/(R_air*C1)-1)
    elif h >= altitude[1] and h < altitude[2]:
        T = temperature[1]
        p = pressure[1]*numpy.exp((-g*(h-altitude[1]))/(R_air*T))
        rho = density[1]*numpy.exp((-g*(h-altitude[1]))/(R_air*T))
    elif h >= altitude[2] and h < altitude[3]:
        T = temperature[2]+C2*(h-altitude[2])
        p = pressure[2]*(T/temperature[2])**((-g)/(R_air*C2))
        rho = density[2]*(T/temperature[2])**((-g)/(R_air*C2)-1)
    elif h >= altitude[3] and h < altitude[4]:
        T = temperature[3]
        p = pressure[3]*numpy.exp((-g*(h-altitude[3]))/(R_air*T))
        rho = density[3]*numpy.exp((-g*(h-altitude[3]))/(R_air*T))
    elif h >= altitude[4] and h < altitude[5]:
        T = temperature[4]+C3*(h-altitude[4])
        p = pressure[4]*(T/temperature[4])**((-g)/(R_air*C3))
        rho = density[4]*(T/temperature[4])**((-g)/(R_air*C3)-1)
    elif h >= altitude[5] and h < altitude[6]:
        T = temperature[5]
        p = pressure[5]*numpy.exp((-g*(h-altitude[5]))/(R_air*T))
        rho = density[5]*numpy.exp((-g*(h-altitude[5]))/(R_air*T))
    elif h >= altitude[6] and h <= altitude[7]:
        T = temperature[6]+C4*(h-altitude[6])
        p = pressure[6]*(T/temperature[6])**((-g)/(R_air*C4))
        rho =  density[6]*(T/temperature[6])**((-g)/(R_air*C4)-1)
    else:
        print("Bad altitude")
        #la funzione exit blocca il calcolo quando si verifica questa condizione###
        sys.exit()
    return(T, p, rho)

f = p_rho_T(5145.33827284, "hG")  
#print(f)


# plot ################################################################

h = numpy.linspace(0.0, 105.0e3, 10000)
T = numpy.zeros_like(h)
p = numpy.zeros_like(h)
rho = numpy.zeros_like(h)

for k in range(0, len(h), 1):
    T_k, p_k, rho_k = p_rho_T(h[k])
    p[k] = p_k
    T[k] = T_k
    rho[k] = rho_k

x = T
y = h

plt.xlabel('Temperatura [k]')
plt.ylabel('altitudine [m]')
plt.plot(x,y, color='r', marker='.')
#plt.show()

x1 = p
y1 = h

plt.xlabel('pressione [Pa]')
plt.ylabel('altitudine [m]')
plt.plot(x1, y1, color='b', marker='.')
#plt.show()

x2 = rho
y2 = h

plt.xlabel('densità [kg/m^3]')
plt.ylabel('altitudine [m]')
plt.plot(x2, y2, color='g', marker='.')
#plt.show()

# INSERIRE PLT.SHOW PER VISUALIZZARE I PLOT ########################

T, p, rhoa = p_rho_T(10972.8, "hG")   

rho1 = rhoa

n = -numpy.log(rho1/rho_0)/(10972.8)
  
def rho_n(h_input, h_flag = "hG"):
    if (h_flag == "hG"):
         rE = 6378.0e3
         h = rE*h_input/(rE+h_input)
    else:
        h = h_input
        
    Den = rho_0*numpy.exp(-n*h)
    return(Den)
    sys.exit()

l = rho_n(10972.8)
#print(l)

# CONVERSIONE QUOTE [m] -> [ft]

def hft(h):
    
    hft = h*(3.281)
    return(hft)
    sys.exit()
    
hf = hft(1.0)
#print(hf)
    
# DENSITA' A QUOTE OBIETTIVO ########################################

Q1 = hft(5000)
Q2 = hft(10000)
Q3 = hft(20000)
Q4 = hft(30000)
Q5 = hft(40000)

# print(Q1 ,Q2, Q3, Q4, Q5)

rn1 = rho_n(Q1)
rn2 = rho_n(Q2)
rn3 = rho_n(Q3)
rn4 = rho_n(Q4)
rn5 = rho_n(Q5)

# print(rn1, rn2, rn3, rn4, rn5)

# DENSITY AND TEMPERATURE ALTITUDE ##################################

def T_p_rho_altitude(h_T, T_input, p_input, rho_input):
    
    T, p, rho = p_rho_T(h_T, h_flag = "hG")
    
    res = T - T_input
    res = rho - rho_input
    res = p - p_input
    
    return(res)
    
h_T_guess = 5000.0
h_rho_guess = 5000.0
h_p_guess = 5000.0
T_input = 253.0
p_input = 53.0e3
rho_input = p_input/(R_air*T_input)
    
sol_T = scipy.optimize.fsolve(T_p_rho_altitude, h_T_guess, args = (T_input, p_input, rho_input))
sol_p = scipy.optimize.fsolve(T_p_rho_altitude, h_p_guess, args = (T_input, p_input, rho_input))
sol_rho = scipy.optimize.fsolve(T_p_rho_altitude, h_rho_guess, args = (T_input, p_input, rho_input))
#print(sol_T, sol_p, sol_rho)
    
    
    




             
