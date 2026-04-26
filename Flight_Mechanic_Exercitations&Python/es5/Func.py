# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:23:55 2023

@author: 39348
"""

import numpy 
import sys


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
def eval_T_P_rho(h_input, h_flag = "hG"):
    
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

f = eval_T_P_rho(10972.8, "hG")    
#print(f)

###############################################################################

def eval_aerodynamic_coefficients(alpha, Re, airfoil):
    filename = airfoil+"_Re"+Re+".txt"
    #print(filename)
    data = numpy.loadtxt(filename, skiprows = 12)
    #print(data[:,0]) #[:,0] printa solo la prima colonna, al posto di questo shape mostrava il numero di righe e colonne
    #print(data[:,1])
    
    alpha_vec = data[:,0]
    CL_vec = data[:,1]
    Cm_vec = data[:,4]
    Cd_vec = data[:,2]
    
    if (alpha < alpha_vec[0]) or (alpha > alpha_vec[-1]): #se inseriamo angoli di attacco non validi, ovvero angoli di attacco più piccoli del valore minore nella tabella o più grande del valore più grande della tabella
        print("Bad angle of attack alpha: ", alpha)
        sys.exit()
        
    i = 0
    while (alpha > alpha_vec[i]): #questo ciclo while ci restituisce la i, ovvero la posizione del primo angolo di attacca maggiore di quello inserito
        i += 1 #i=i+1
        
    alphaL = alpha_vec[i-1] #angolo di attacco della tabella prima del primo più grande di quello inserito
    alphaU = alpha_vec[i] #primo angolo di attacco più grande di quello inserito
    
    CLl = CL_vec[i-1]
    CLU = CL_vec[i]
    
    Cdl = Cd_vec[i-1]
    CdU = Cd_vec[i]
    
    Cml = Cm_vec[i-1]
    CmU = Cm_vec[i]
    
    
    CL = CLl + ((alpha-alphaL)/(alphaU-alphaL))*(CLU-CLl)
    print("CL =", CL)
    
    Cm = Cml + ((alpha-alphaL)/(alphaU-alphaL))*(CmU-Cml)
    print("Cm =", Cm)
    
    Cd = Cdl + ((alpha-alphaL)/(alphaU-alphaL))*(CdU-Cdl)
    print("Cd =", Cd)

    return CL, Cm, Cd
###################################################################################################

