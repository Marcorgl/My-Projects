# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:20:03 2023

@author: 39348
"""

import numpy 
import matplotlib.pyplot as plt 
import math 
from Func import eval_T_P_rho
import scipy.optimize
from sympy import symbols, solve

    
a = input("input the number of question: \n\n") 

if a == "1":
 
    #JET ENGINE  
     
    rho_sl = 1.225 
    S_jet = 48.96 
    cd_0_jet = 0.02 
    lambda_jet = (19.38*19.38)/(48.96) 
    k_jet = 1/(math.pi*0.81*lambda_jet) 
    W_jet = 16193.248*9.81  
     
    V_jet= numpy.linspace(20, 316.48, 1000) 
     
    a_T_jet = (rho_sl*S_jet*cd_0_jet)/2 
    b_T_jet = (2*k_jet*S_jet)/rho_sl 
    c_T_jet = (numpy.power((W_jet/S_jet),2))
     
     
    T_req_jet = (a_T_jet*numpy.power(V_jet,2))+((b_T_jet*c_T_jet)*(1/(numpy.power(V_jet,2)))) 
    P_req_jet = T_req_jet*V_jet 
    
    V_Tmin_jet = math.sqrt((2*W_jet)/(rho_sl*S_jet))*numpy.power((k_jet)/(cd_0_jet),1/4) 
    V_Pmin_jet = V_Tmin_jet*0.76  
    
     
    fig = plt.figure() 
    ax = fig.gca() 
     
    ax.plot(V_jet,T_req_jet, label = "T_req_jet", marker = ",") 
     
    ax.set_xlabel(r"$V_jet$") 
    ax.set_ylabel(r"$T_req_jet$") 
     
    ax.legend() 
    ax.set_title("T_req_jet at sea level") 
     
    plt.show() 
     
    fig = plt.figure() 
    ax = fig.gca() 
     
    ax.plot(V_jet, P_req_jet, label = "P_req_jet", marker = ",") 
     
    ax.set_xlabel(r"$V_jet$") 
    ax.set_ylabel(r"$P_req_jet$") 
     
    ax.legend() 
    ax.set_title("P_req_jet at sea level") 
     
    plt.show() 
     
    print("V_Tmin_jet: ",V_Tmin_jet) 
    print("V_Pmin_jet:",V_Pmin_jet) 
     
     
    ############################################################################################################################################################################ 
     
    #PROP ENGINE 
      
    S_prop = 14.77 
    cd_0_prop = 0.025 
    lambda_prop = (11.03*11.03)/(14.77) 
    k_prop = 1/(math.pi*0.8*lambda_prop) 
    W_prop = 1133.98*9.81
     
    V_prop = numpy.linspace(3,81.36,1000) 
     
    a_T_prop = (rho_sl*S_prop*cd_0_prop)/2 
    b_T_prop = (2*k_prop*S_prop)/rho_sl 
    c_T_prop = (numpy.power((W_prop/S_prop),2)) 
    
    T_req_prop = (a_T_prop*numpy.power(V_prop, 2))+((b_T_prop*c_T_prop)*(1/(numpy.power(V_prop, 2)))) 
    P_req_prop = (T_req_prop*V_prop)*0.8 
    
    V_Tmin_prop = math.sqrt((W_prop)/(rho_sl*S_prop))*numpy.power((4*k_prop)/(cd_0_prop),1/4) 
    V_Pmin_prop = 0.76*V_Tmin_prop 
     
    fig = plt.figure() 
    ax = fig.gca() 
     
    ax.plot(V_prop, T_req_prop, label = "T_req_prop", marker = ",") 
     
    ax.set_xlabel(r"$V_prop$") 
    ax.set_ylabel(r"$T_req_prop$") 
     
    ax.legend() 
    ax.set_title("T_req_prop at sea level") 
     
    plt.show() 
     
    
    fig = plt.figure() 
    ax = fig.gca() 
      
    ax.plot(V_prop, P_req_prop, label = "P_req_prop", marker = ",") 
      
    ax.set_xlabel(r"$V_prop$") 
    ax.set_ylabel(r"$P_req_prop$") 
      
    ax.legend() 
    ax.set_title("P_req_prop at sea level") 
      
    plt.show() 
    
    
    print("V_Tmin_prop: ",V_Tmin_prop) 
    print("V_Pmin_prop: ",V_Pmin_prop) 
     
    ########################################################################################################################### 
     
    T, P, rho = eval_T_P_rho(5000) 
     
    rho_h = rho 
      
    a_T_jet_h = (rho_h*S_jet*cd_0_jet)/2 
    b_T_jet_h = (2*k_jet*S_jet)/rho_h 
    c_T_jet_h = (numpy.power((W_jet/S_jet),2)) 
    
    T_req_jet_h = (a_T_jet_h*numpy.power(V_jet,2))+((b_T_jet_h*c_T_jet_h)*(1/(numpy.power(V_jet,2)))) 
    P_req_jet_h = T_req_jet_h*V_jet
     
    fig = plt.figure() 
    ax = fig.gca() 
     
    ax.plot(V_jet,T_req_jet_h, label = "T_req_jet_h", marker = ",") 
     
    ax.set_xlabel(r"$V_jet_h$") 
    ax.set_ylabel(r"$T_req_jet_h$") 
     
    ax.legend() 
    ax.set_title("T_req_jet at 5000m") 
     
    plt.show() 
     
     
    fig = plt.figure() 
    ax = fig.gca() 
     
    ax.plot(V_jet, P_req_jet_h, label = "P_req_jet_h", marker = ",") 
     
    ax.set_xlabel(r"$V_jet_h$") 
    ax.set_ylabel(r"$P_req_jet_h$") 
     
    ax.legend() 
    ax.set_title("P_req_jet at 5000m") 
     
    plt.show() 
     
    ############################################################################################################################# 
     
    fig20 = plt.figure() 
    ax20 = fig20.gca() 
    ax20.plot(V_jet,T_req_jet, label = "sea level") 
    ax20.plot(V_jet,T_req_jet_h, label = "5000m") 
    ax20.set_xlabel(r"$V_jet$") 
    ax20.set_ylabel(r"$T_req$") 
    ax20.legend() 
    ax20.set_title("T_req_jet(h)") 
     
    plt.show() 
     
     
    fig20 = plt.figure() 
    ax20 = fig20.gca() 
    ax20.plot(V_jet, P_req_jet, label = "sea level") 
    ax20.plot(V_jet, P_req_jet_h, label = "5000m") 
    ax20.set_xlabel(r"$V_jet$") 
    ax20.set_ylabel(r"$P_req$") 
    ax20.legend() 
    ax20.set_title("P_req_jet(h)") 
     
    plt.show() 
     
    ############################################################################################################################### 
     
    V_prop_T = numpy.linspace(20, 316.48, 1000) 
     
    a_T_prop_h = (rho_h*S_prop*cd_0_prop)/2 
    b_T_prop_h = (2*k_prop*S_prop)/rho_h 
    c_T_prop_h = (numpy.power((W_prop/S_prop),2)) 
    
    T_req_prop_h = (a_T_prop_h*numpy.power(V_prop_T,2))+((b_T_prop_h*c_T_prop_h)*(1/(numpy.power(V_prop_T,2)))) 
    P_req_prop_h = (T_req_prop_h*V_prop)/0.8 
     
    fig = plt.figure() 
    ax = fig.gca() 
     
    ax.plot(V_prop_T,T_req_prop_h, label = "T_req_prop_h", marker = ",") 
     
    ax.set_xlabel(r"$V_prop$") 
    ax.set_ylabel(r"$T_req_prop_h$") 
     
    ax.legend() 
    ax.set_title("T_req_prop at 5000m") 
     
    plt.show() 
     
    
    fig = plt.figure() 
    ax = fig.gca() 
     
    ax.plot(V_prop, P_req_prop_h, label = "P_req_prop_h", marker = ",") 
     
    ax.set_xlabel(r"$V_prop$") 
    ax.set_ylabel(r"$P_req_prop_h$") 
     
    ax.legend() 
    ax.set_title("P_req_prop at 5000m") 
     
    plt.show() 
     
    ###################################################################################################### 
     
    fig20 = plt.figure() 
    ax20 = fig20.gca() 
    ax20.plot(V_prop_T,T_req_prop, label = "sea level") 
    ax20.plot(V_prop_T,T_req_prop_h, label = "5000m") 
    ax20.set_xlabel(r"$V_prop$") 
    ax20.set_ylabel(r"$T_req$") 
    ax20.legend() 
    ax20.set_title("T_req_prop(h)") 
     
    plt.show() 
     
     
    fig20 = plt.figure() 
    ax20 = fig20.gca() 
    ax20.plot(V_prop, P_req_prop, label = "sea level") 
    ax20.plot(V_prop, P_req_prop_h, label = "5000m") 
    ax20.set_xlabel(r"$V_prop$") 
    ax20.set_ylabel(r"$P_req$") 
    ax20.legend() 
    ax20.set_title("P_req_prop(h)") 
     
    plt.show()
    
    T_av_0= 30087.77109348909*2
 
    T,P,rho= eval_T_P_rho(5000,h_flag="hG") 
    rho_h_1= rho 
    T_av_1= (rho_h_1/rho_sl)*T_av_0 
    V_jet_T_real= numpy.linspace(69.96,316.48,1000) 
     
    T_req_jet_h_real = (a_T_jet_h*numpy.power(V_jet_T_real,2))+((b_T_jet_h*c_T_jet_h)*(1/(numpy.power(V_jet_T_real,2)))) 
    T_req_jet_real = (a_T_jet*numpy.power(V_jet_T_real,2))+((b_T_jet*c_T_jet)*(1/(numpy.power(V_jet_T_real,2)))) 
     
    fig20 = plt.figure() 
    ax20 = fig20.gca() 
    ax20.plot(V_jet_T_real, T_req_jet_real, label = "sea level") 
    ax20.plot(V_jet_T_real, T_req_jet_h_real, label = "5000m") 
    ax20.plot(V_jet, T_av_1, label = "5000m") 
    ax20.plot(V_jet, T_av_0, label = "sea level") 
    ax20.plot(V_jet, T_req_jet, label = "sea level", linestyle = "--") 
    ax20.plot(V_jet, T_req_jet_h, label = "5000m", linestyle = "--") 
    ax20.set_xlabel(r"$V_jet$") 
    ax20.set_ylabel(r"$T_req$") 
    ax20.legend() 
    ax20.set_title("T_req_jet(h)") 

elif a == "2":
    def absolute_ceiling_jet(x):
        
        h_T = x
        T, p, rho_h = eval_T_P_rho(h_T) 
        rho_sl = 1.225
        cd_0_jet = 0.02 
        lambda_jet = (19.38*19.38)/(48.96) 
        k_jet = 1/(math.pi*0.81*lambda_jet) 
        W_jet = 16193.248*9.81   
        
        T_max_sl = 2*30087.77109348909
        
        T_av =  (rho_h/rho_sl)*T_max_sl
        T_min = 2*W_jet*numpy.power(cd_0_jet*k_jet, 1/2)
        
        eq = (T_av - T_min)/W_jet
        return eq
    
    x01 = 15000
        
    ab_cie2 = scipy.optimize.fsolve(absolute_ceiling_jet, x01)
    print(f"\n The absolute cieling of jet is : {ab_cie2}\n\n")
    
    S_jet = 48.96 
    cd_0_jet = 0.02
    lambda_jet = (19.38*19.38)/(48.96) 
    k_jet = 1/(math.pi*0.81*lambda_jet) 
    W_jet = 16193.248*9.81   
    V_jet= numpy.linspace(20, 316.48, 1000)  #HO INSERITO 100 PER PLOTTARE MEGLIO IL GRAFICO
    T_max_sl = 2*30087.77109348909
    rho_sl = 1.225
    
    T, P, rho = eval_T_P_rho(ab_cie2) 
     
    rho_h = rho 
      
    a_T_jet_h = (rho_h*S_jet*cd_0_jet)/2 
    b_T_jet_h = (2*k_jet*S_jet)/rho_h 
    c_T_jet_h = (numpy.power((W_jet/S_jet),2)) 
    
    T_req_jet_h = (a_T_jet_h*numpy.power(V_jet,2))+((b_T_jet_h*c_T_jet_h)*(1/(numpy.power(V_jet,2)))) 
    
    T_req_ab = (rho/rho_sl)*T_max_sl
     
    fig = plt.figure() 
    ax = fig.gca() 
     
    ax.plot(V_jet, T_req_jet_h, label = f"T_req_jet_h: {ab_cie2[0]:.3e}", marker = ",") 
    
    ax.set_xlabel("V_jet") 
    ax.set_ylabel(f"T_req_jet_h: {ab_cie2[0]:.3e}") 
    ax.axhline(T_req_ab, color='orange')
    ax.set_title("T_req_jet at absolute cieling") 
     
    plt.show() 
    
    print(f"Tmin required at absolute cieling is: {T_req_ab}")
    
    h_array = numpy.linspace(0, ab_cie2[0], 100)
    Vmin = numpy.zeros_like(h_array)
    Vmax = numpy.zeros_like(h_array)
    
    for k in range(0, len(h_array), 1):
        
        T_k, p_k, rho = eval_T_P_rho(h_array[k])
        
        a_T_jet_h = (rho*S_jet*cd_0_jet)/2 
        b_T_jet_h = (2*k_jet*S_jet)/rho
        c_T_jet_h = (numpy.power((W_jet/S_jet),2)) 
        
        T_max_sl = 2*30087.77109348909
        
        T_av = (rho/rho_sl)*T_max_sl
        
        Vmin[k] = numpy.power((T_av/(2*a_T_jet_h))*(1-numpy.power(1-((4*a_T_jet_h*b_T_jet_h*c_T_jet_h)/(T_av**2)), 1/2)), 1/2)
        Vmax[k] = numpy.power((T_av/(2*a_T_jet_h))*(1+numpy.power(1-((4*a_T_jet_h*b_T_jet_h*c_T_jet_h)/(T_av**2)), 1/2)), 1/2)
    
    
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(h_array, Vmin , label = "Vmin(h)", marker = ",")
    ax.set_title("Vmin(h)")
    plt.xlabel("altitude")
    plt.ylabel("Vmin")
    
    plt.show()
    
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(h_array, Vmax , label = "Vmax(h)", marker = ",")
    ax.set_title("Vmax(h)")
    plt.xlabel("altitude")
    plt.ylabel("Vmax")
    
    plt.show()
    
    
    rho4 = 0.8192289609615372 #A 4Km
    V_Tmin_jet1 = math.sqrt((W_jet)/(rho4*S_jet))*numpy.power((4*k_jet)/(cd_0_jet),1/4) 
     
    print(f"V_Tmin_jet is : {V_Tmin_jet1}") 
     
    V_Pmin_jet1 = V_Tmin_jet1*0.76 
     
    print(f"V_Pmin_jet is : {V_Pmin_jet1}") 
    
    V_maxR = V_Tmin_jet1*1.316
    
    print(f"V_maxR is: {V_maxR}")
    
    T, P, rho = eval_T_P_rho(4000)  
     
    V_jet_T1= numpy.linspace(3,316.48,1000) 
     
    a_T_jet_h = (rho4*S_jet*cd_0_jet)/2 
    b_T_jet_h = (2*k_jet*S_jet)/rho4 
    c_T_jet_h = (numpy.power((W_jet/S_jet),2)) 
     
     
    T_req_jet_h5 = (a_T_jet_h*numpy.power(V_jet_T1,2))+((b_T_jet_h*c_T_jet_h)*(1/(numpy.power(V_jet_T1,2)))) 
     
    fig = plt.figure() 
    ax = fig.gca() 
    ax.set_xlabel(r"$V_jet_h$") 
    ax.set_ylabel(r"$T_req_jet_h$") 
     
    ax.legend() 
    ax.set_title("T_req_jet at 4000m")
    ax.plot(V_jet_T1,T_req_jet_h5, label = "T_req_jet_h") 
    
    plt.axvline(x = V_Tmin_jet1, color="red", label = " V_Tmin_jet")
    plt.axvline(x = V_Pmin_jet1, color="green", label = "V_Pmin_jet")
    plt.axvline(x = V_maxR, color="cyan", label = "V_maxR" )
    plt.legend()
    plt.show()

        
elif a == "3":    
    def absolute_ceiling_prop(x):
        
        h_T = x
        T, p, rho_h = eval_T_P_rho(h_T)
        PAmax_sl = 171510.97046*0.8
        W_prop = 9.81*1133.980925
        S_prop = 14.7716
        lambda_prop = (11.0338**2) / (14.7716)
        k_prop = 1 / (math.pi * 0.8 * lambda_prop)
        rho_sl = 1.225
        cd_0_prop = 0.025
        
        p_min = 4 * W_prop*(numpy.power(cd_0_prop * numpy.power(k_prop / 3, 3), (1 / 4)) * numpy.power((2 * W_prop) / (rho_h * S_prop), (1/2)))
        
        p_av = ((rho_h/rho_sl) - ((1-(rho_h/rho_sl))/7.55))*PAmax_sl
        
        eq = (p_av - p_min)
        return eq
    
    x0 = 5000
        
    ab_cie = scipy.optimize.fsolve(absolute_ceiling_prop, x0)
    print(f"\n\n The absolute cieling of propeller is : {ab_cie}\n")
    
    rho5 = 0.49199391232911505
    
    PAmax_sl = 171510.97046*0.8
    W_prop = 9.81*1133.980925
    S_prop = 14.7716
    lambda_prop = (11.0338**2) / (14.7716)
    k_prop = 1 / (math.pi * 0.8 * lambda_prop)
    rho_sl = 1.225
    cd_0_prop = 0.025
    V_prop_T = numpy.linspace(6,81.36,1000)
    
    a_T_prop_h = (rho5*S_prop*cd_0_prop)/2 
    b_T_prop_h = (2*k_prop*S_prop)/rho5 
    c_T_prop_h = (numpy.power((W_prop/S_prop),2))
    
    T, P, rho = eval_T_P_rho(ab_cie) 
     
    rho_h = rho
    
    T_req_prop_h8 = (a_T_prop_h*numpy.power(V_prop_T,2))+((b_T_prop_h*c_T_prop_h)*(1/(numpy.power(V_prop_T,2)))) 
    P_req_prop_h8 = (T_req_prop_h8*V_prop_T)/0.8
    
    P_av8 = ((rho5/rho_sl)-((1-(rho5/rho_sl))/7.55))*171511
    
    fig = plt.figure() 
    ax = fig.gca() 
     
    ax.plot(V_prop_T,P_req_prop_h8, label = f"P_prop_jet_h: {ab_cie[0]:.3e}", marker = ",") 
    
    ax.set_xlabel("V_prop") 
    ax.set_ylabel(f"P_req_prop_h8: {ab_cie[0]:.3e}") 
    ax.axhline(P_av8, color='orange')
    ax.legend() 
    ax.set_title("P_req_prop at absolute cieling") 
     
    plt.show()

##########################################

    
    V_prop = symbols('V_prop')
    
    h_array = numpy.linspace(0, ab_cie[0], 100)
    Vmin = numpy.zeros_like(h_array)
    Vmax = numpy.zeros_like(h_array)
    
    for k in range(0, len(h_array), 1):
        T, p, rho_h = eval_T_P_rho(h_array[k])
    
        PAmax_sl = 171510.97046 * 0.8
        P_shaft = ((rho_h / rho_sl) - ((1 - (rho_h / rho_sl)) / 7.55)) * PAmax_sl
        eta_shaft = 0.8
        A = (rho_h * S_prop * cd_0_prop) / 2
        B = ((2 * k_prop * S_prop) / rho_h) * (numpy.power((W_prop / S_prop), 2))
    
        pol = V_prop**4 - ((eta_shaft * P_shaft) / A) * V_prop + B / A
        radici = solve(pol, V_prop)
    
        # Filtra solo le soluzioni reali
        radici_real = [radice for radice in radici if radice.is_real]
    
        if radici_real:
            Vmin[k] = min(radici_real)
            Vmax[k] = max(radici_real)
        else:
            # Gestisci il caso in cui non ci sono soluzioni reali
            Vmin[k] = numpy.nan
            Vmax[k] = numpy.nan

    
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(h_array, Vmin, marker = ",", label = "Vmin")
    ax.set_title("Vmin(h)")
    ax.set_xlabel("altitude")
    ax.set_ylabel("Vmin")
    plt.show()
    
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(h_array, Vmax, marker = ",", label = "Vmax")
    ax.set_title("Vmax(h)")
    ax.set_xlabel("altitude")
    ax.set_ylabel("Vmax")
    plt.show()
            
        
    rho4 = 0.8192289609615372 #A 4Km
    V_Tmin_prop1 = math.sqrt((W_prop)/(rho4*S_prop))*numpy.power((4*k_prop)/(cd_0_prop),1/4) 
     
    print(f"V_Tmin_prop is : {V_Tmin_prop1} ") 
     
    V_Pmin_prop1 = V_Tmin_prop1*0.76 
     
    print(f"V_Pmin_prop is : {V_Pmin_prop1}") 
    
    V_maxR_prop = V_Tmin_prop1
    
    print(f"V_maxR_prop is: {V_maxR_prop}")
    
    T, P, rho = eval_T_P_rho(4000)  
     
    V_prop_T1= numpy.linspace(3,316.48,1000) 
     
    a_T_prop_h = (rho4*S_prop*cd_0_prop)/2 
    b_T_prop_h = (2*k_prop*S_prop)/rho4 
    c_T_prop_h = (numpy.power((W_prop/S_prop),2)) 
     
     
    T_req_prop_h5 = (a_T_prop_h*numpy.power(V_prop_T1,2))+((b_T_prop_h*c_T_prop_h)*(1/(numpy.power(V_prop_T1,2)))) 
     
    fig = plt.figure() 
    ax = fig.gca() 
    ax.set_xlabel(r"$V_prop_h$") 
    ax.set_ylabel(r"$P_req_prop_h$") 
     
    ax.legend() 
    ax.set_title("P_req_prop at 4000m")
    ax.plot(V_prop_T1,T_req_prop_h5, label = "P_req_prop_h") 
    
    plt.axvline(x = V_Tmin_prop1, color="red", label = " V_Tmin_prop = Vmax_R")
    plt.axvline(x = V_Pmin_prop1, color="green", label = "V_Pmin_prop")
    plt.legend()
    plt.show()
    
    

