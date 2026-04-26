# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:00:35 2023

@author: 39348
"""

import numpy 
import matplotlib.pyplot as plt

from Func import eval_aerodynamic_coefficients

Re_array = [5e4, 2e5, 1e6]

c = 1.3
pho_sl = 1.225
mi_sl = 1.789e-5

n = 100
alpha = numpy.linspace(-8.0, 12.0, num = n)

for k in Re_array:
    Cl_Rek = numpy.zeros_like(alpha)
    Cm_Rek = numpy.zeros_like(alpha)
    Cd_Rek = numpy.zeros_like(alpha)
    l_Rek = numpy.zeros_like(alpha)
    d_Rek = numpy.zeros_like(alpha)
    m_Rek = numpy.zeros_like(alpha)
    V_k = (float(k)*mi_sl)/(pho_sl*c)
    for i in range(n):
        a = '{:.0e}'.format(k)
        b = a.replace('+', '')
        Cl_i, Cm_i, Cd_i = eval_aerodynamic_coefficients (alpha[i], Re = b.replace('0', '') , airfoil = 'NACA2412')
        Cl_Rek[i] = Cl_i
        Cm_Rek[i] = Cm_i
        Cd_Rek[i] = Cd_i
        l_Rek[i] = (1/2) * pho_sl * c * Cl_i * (V_k**2)
        d_Rek[i] = (1/2) * pho_sl * c * Cd_i * (V_k**2)
        m_Rek[i] = (1/2) * pho_sl * c * Cm_i * (V_k**2)
        
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(alpha, Cl_Rek, color='r', marker=',')
    ax.set_title("Cl_"+b.replace('0', '')+" vs Alpha")
    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(0, color='black', linestyle='--')
    plt.xlabel('Alpha')
    plt.ylabel('Cl')
    plt.show()
    
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(alpha, Cm_Rek, color='g', marker=',')
    ax.set_title("Cm_Re"+b.replace('0', '')+" vs Alpha")
    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(0, color='black', linestyle='--')
    plt.xlabel('Alpha')
    plt.ylabel('Cm')
    plt.show()  
    
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(alpha, Cd_Rek, color='b', marker=',')
    ax.set_title("Cd_Re"+b.replace('0', '')+" vs Alpha")
    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(0, color='black', linestyle='--')
    plt.xlabel('Alpha')
    plt.ylabel('Cd')
    plt.show()
    
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(Cd_Rek, Cl_Rek, color='purple', marker=',')
    ax.set_title("Polare_Re"+b.replace('0', ''))
    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(0, color='black', linestyle='--')
    plt.xlabel('Cd')
    plt.ylabel('Cl')
    plt.show()

    fig = plt.figure()
    ax = fig.gca()
    ax.plot(alpha, l_Rek, color = "brown", marker =",")
    ax.set_title("lift_unit_span_"+b.replace('0', ''))
    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(0, color='black', linestyle='--')
    plt.xlabel('alpha')
    plt.ylabel('l_unit_span_')
    plt.show()
    
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(alpha, d_Rek, color = "orange", marker =",")
    ax.set_title("drag_unit_span_"+b.replace('0', ''))
    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(0, color='black', linestyle='--')
    plt.xlabel('alpha')
    plt.ylabel('d_unit_span_')
    plt.show()
    
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(alpha, m_Rek, color = "pink", marker =",")
    ax.set_title("moment_unit_span_"+b.replace('0', ''))
    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(0, color='black', linestyle='--')
    plt.xlabel('alpha')
    plt.ylabel('m_unit_span_')
    plt.show()
    

    



