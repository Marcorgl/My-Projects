# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# IMPORTARE LA FUNZIONE ###############################

from Func import p_rho_T
import math
import scipy
import numpy 
from matplotlib import pyplot as plt
import sys
import scipy.optimize

# DATA ############################################################

g = 9.81
R_air = 287.07 
rho_sl = 1.225
p_sl = 101.3e3
p_0 = 4.24e4
gamma = 1.4

# SPEED OF SOUND ##################################################

T_10km, p_10km, rho_10km = p_rho_T(10)
#print(T_10km, p_10km, rho_10km)

a = (1.4*T_10km*R_air)**(1/2) 
#print(a)

# MACH ############################################################

M = ((2)/((gamma-1))*((((p_0/p_10km))**((gamma-1)/gamma))-1))**(1/2)
#print(M)

# VTAS AND VCAS ####################################################

T = 230
rho = p_10km/(R_air*T)

VTAS = a*M
#print(VTAS)

VCAS = (((2*gamma*p_sl)/((gamma-1)*rho_sl))*(((((p_0-p_10km)/p_sl)+1)**((gamma-1)/gamma))-1))**(1/2)
#print(VCAS)

# DIFFERENCE BETWEEN TRUE AND CALIBRATED AS ########################

diff_perc = ((VTAS-VCAS)/VTAS)*100
#print(diff_perc)

# ERROR COMPRESSIBLE VS INCOMPRESSIBILE #############################

VTAS_comp = ((2*(p_0-p_10km))/rho_10km)**(1/2)

err = (VTAS_comp-VTAS)/(VTAS_comp)*100
#7print(err)

#### FUNC_SPEED #####################################################

def all_speed(h_p, p_st, T_air):
    
    T, p, rho = p_rho_T(h_p)
    
    M_f = ((2)/((gamma-1))*((((p_st/p))**((gamma-1)/gamma))-1))**(1/2)
    
    a = (gamma*T_air*R_air)**(1/2)
    
    if M_f < 0.3:
        
        VTAS_f = a*M_f
        VEAS_f = VTAS_f*((rho/rho_sl)**(1/2))
        VCAS_f = " Not defined "
        
    else: 
        
        VTAS_f = a*M_f
        VEAS_f = VTAS_f*(rho/rho_sl)**(1/2)
        VCAS_f = (((2*gamma*p_sl)/((gamma-1)*rho_sl))*(((((p_st-p)/p_sl)+1)**((gamma-1)/gamma))-1))**(1/2)
        
    return(VTAS_f, VEAS_f, VCAS_f)
    sys.exit()

VTAS_f, VEAS_f, VCAS_f = all_speed(10, 180.4e3 , 230)
#print(VTAS_f, VEAS_f, VCAS_f)
    
    