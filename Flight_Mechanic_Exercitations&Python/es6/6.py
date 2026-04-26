# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:58:26 2023

@author: 39348
"""

import numpy 
import matplotlib.pyplot as plt 
import math 
from Func import eval_T_P_rho
from sympy import symbols, solve

#Question 1

#Angle of climb jet at sea level

hG = 0 
rho_sl = 1.225 
V_jet_T = numpy.linspace(30, 310, 1000) 
 
S_jet = 48.96 
cd_0_jet = 0.02 
lambda_jet = (19.38*19.38)/(48.96) 
k_jet = 1/(math.pi*0.81*lambda_jet) 
W_jet = 16193.248*9.81 

a_T_jet_0 = (rho_sl*S_jet*cd_0_jet)/2 
b_T_jet_0 = (2*k_jet*S_jet)/rho_sl 
c_T_jet_0 = (numpy.power((W_jet/S_jet),2)) 
  

T_av_0 = 60134.74   

CL_0 = (2*W_jet)/(rho_sl*S_jet*numpy.power(V_jet_T,2)) 
CD_0 = cd_0_jet+k_jet*(numpy.power(CL_0, 2)) 
E = CL_0/CD_0 
 
AoC_0_jet = ((T_av_0/W_jet)-(1/(E)))*(180/math.pi)
 
fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_jet_T, AoC_0_jet, label = "AoC_0_jet") 
 
ax.set_xlabel("V_jet") 
ax.set_ylabel("AoC_jet") 
 
ax.legend() 
ax.set_title("Angle of climb jet at sea level") 

plt.show()

#######################################################################################################

#Angle of climb jet at 11000ft

V_jet_T_1 = numpy.linspace(40, 310, 1000) 

hG_1 = 3352.8 
T, P, rho = eval_T_P_rho(hG_1, h_flag="hG") 
rho_1 = rho 
 
      
a_T_jet_1 = (rho_1*S_jet*cd_0_jet)/2 
b_T_jet_1 = (2*k_jet*S_jet)/rho_1 
c_T_jet_1 = (numpy.power((W_jet/S_jet),2)) 
  
 
 
T_av_1 = (rho_1/rho_sl)*T_av_0 
  
CL_1 = (2*W_jet)/(rho_1*S_jet*numpy.power(V_jet_T_1, 2)) 
CD_1 = cd_0_jet+k_jet*(numpy.power(CL_1, 2)) 
E = CL_1/CD_1 
 
AoC_1_jet = ((T_av_1/W_jet)-(1/(E)))*(180/math.pi) 
 
fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_jet_T_1, AoC_1_jet, label = "AoC_jet") 
 
ax.set_xlabel("V_jet") 
ax.set_ylabel("AoC_jet") 
 
ax.legend() 
ax.set_title("Angle of climb jet at 11000 ft") 
 
plt.show() 

################################################################################################################################

#Angle of climb jet at 22000ft

 
hG_2 = 6705.6 
T,P,rho = eval_T_P_rho(hG_2,h_flag="hG") 
rho_2 = rho 
 
 
V_jet_T_2 = numpy.linspace(50,316.48,1000) 
   
  
a_T_jet_2 = (rho_2*S_jet*cd_0_jet)/2 
b_T_jet_2 = (2*k_jet*S_jet)/rho_2 
c_T_jet_2 = (numpy.power((W_jet/S_jet),2)) 
   
 
T_av_2 = (rho_2/rho_sl)*T_av_0 
  
CL_2 = (2*W_jet)/(rho_2*S_jet*numpy.power(V_jet_T_2,2)) 
CD_2 = cd_0_jet+k_jet*(numpy.power(CL_2,2)) 
E = CL_2/CD_2 
 
AoC_2_jet = ((T_av_2/W_jet)-(1/(E)))*(180/math.pi)
 
fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_jet_T_2, AoC_2_jet, label = "AoC_jet") 
 
ax.set_xlabel("V_jet") 
ax.set_ylabel("AoC_jet") 
 
ax.legend() 
ax.set_title("Angle of climb jet at 22000 ft") 
 
plt.show() 

#################################################################################################################################


fig = plt.figure() 
ax = fig.gca() 

ax.plot(V_jet_T, AoC_0_jet, label = "AoC_0ft") 
ax.plot(V_jet_T_1, AoC_1_jet, label = "AoC_11000ft") 
ax.plot(V_jet_T_2, AoC_2_jet, label = "AoC_22000ft") 
 
ax.set_xlabel("V_jet") 
ax.set_ylabel("AoC_jet") 
 
ax.legend() 
ax.set_title("Angle of climb jet(h)") 
 
plt.show() 


###################################################################################################################################

#Rate of climb jet at sea level

hG = 0 
rho_sl = 1.225 

    
 
T_req_jet_0 = (a_T_jet_0*numpy.power(V_jet_T,2))+((b_T_jet_0*c_T_jet_0)*(1/(numpy.power(V_jet_T,2)))) 
 
T_av_0 = 60134.74  
  
CL_0 = (2*W_jet)/(rho_sl*S_jet*numpy.power(V_jet_T,2)) 
CD_0 = cd_0_jet+k_jet*(numpy.power(CL_0,2)) 
E = CL_0/CD_0 
 
RoC_0_jet= ((T_av_0-T_req_jet_0)*V_jet_T)/W_jet 
 
fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_jet_T,RoC_0_jet, label = "RoC_jet_0ft") 
 
ax.set_xlabel("V_jet") 
ax.set_ylabel("RoC_jet_0ft") 
 
ax.legend() 
ax.set_title("Rate of climb jet at sea level") 
 
plt.show() 

#####################################################################################################################################

#Rate of climb jet at 11000ft


hG_1 = 3352.8 
T,P,rho = eval_T_P_rho(hG_1,h_flag="hG") 
rho_1 = rho 

  
T_req_jet_1 = (a_T_jet_1*numpy.power(V_jet_T_1,2))+((b_T_jet_1*c_T_jet_1)*(1/(numpy.power(V_jet_T_1,2)))) 
 
T_av_1= (rho_1/rho_sl)*T_av_0 
 
CL_1 = (2*W_jet)/(rho_1*S_jet*numpy.power(V_jet_T_1,2)) 
CD_1 = cd_0_jet+k_jet*(numpy.power(CL_1,2)) 
E = CL_1/CD_1 
 
RoC_1_jet = ((T_av_1-T_req_jet_1)*V_jet_T_1)/W_jet 
 
fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_jet_T_1,RoC_1_jet, label = "RoC_jet_11000ft") 
 
ax.set_xlabel("V_jet") 
ax.set_ylabel("RoC_jet_11000ft") 
 
ax.legend() 
ax.set_title("Rate of climb jet at 11000ft") 
 
plt.show() 
 
#####################################################################################################################################

#Rate of climb jet 22000 ft 


hG_2 = 6705.6 
T,P,rho = eval_T_P_rho(hG_2,h_flag="hG") 
rho_2 = rho 
 
T_req_jet_2 = (a_T_jet_2*numpy.power(V_jet_T_2,2))+((b_T_jet_2*c_T_jet_2)*(1/(numpy.power(V_jet_T_2,2)))) 
  
T_av_2 = (rho_2/rho_sl)*T_av_0 
 
CL_2 = (2*W_jet)/(rho_2*S_jet*numpy.power(V_jet_T_2,2)) 
CD_2 = cd_0_jet+k_jet*(numpy.power(CL_2,2)) 
E = CL_2/CD_2 
 
RoC_2_jet = ((T_av_2-T_req_jet_2)*V_jet_T_2)/W_jet 
 
fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_jet_T_2, RoC_2_jet, label = "RoC_jet_22000ft") 
 
ax.set_xlabel("V_jet") 
ax.set_ylabel("RoC_jet_22000ft") 
 
ax.legend() 
ax.set_title("Rate of climb jet at 22000ft") 
 
plt.show() 


######################################################################################################################################

fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_jet_T,RoC_2_jet, label = "RoC_jet_0ft") 
ax.plot(V_jet_T_1,RoC_0_jet, label = "RoC_jet_11000ft") 
ax.plot(V_jet_T_2,RoC_1_jet, label = "RoC_jet_22000ft") 
 
ax.set_xlabel("V_jet") 
ax.set_ylabel("RoC_jet") 
 
ax.legend() 
ax.set_title("Rate of climb jet(h)") 
 
plt.show()

####################################################################################################################################

#Angle of climb prop at sea level

hG = 0
rho_sl = 1.225
S_prop = 14.77
cd_0_prop = 0.025
lambda_prop = (11.03*11.03)/(14.77)
k_prop = 1/(math.pi*0.8*lambda_prop)
W_prop = 1133.98*9.81

P_av_0_prop = 171510.977*0.8

V_prop_T = numpy.linspace(6, 80, 1000)

a_T_prop = (rho_sl*S_prop*cd_0_prop)/2
b_T_prop = (2*k_prop*S_prop)/rho_sl
c_T_prop = (numpy.power((W_prop/S_prop),2))


T_av_0_prop = P_av_0_prop/V_prop_T
T_req_prop = (a_T_prop*numpy.power(V_prop_T,2))+((b_T_prop*c_T_prop)*(1/(numpy.power(V_prop_T,2))))
P_req_prop = T_req_prop*V_prop_T

AoC_0_prop = ((P_av_0_prop-P_req_prop)/(W_prop*V_prop_T))*(180/math.pi)

fig = plt.figure()
ax = fig.gca()

ax.plot(V_prop_T,AoC_0_prop, label = "AoC_prop_0m")

ax.set_xlabel("V_prop")
ax.set_ylabel("AoC_prop_0m")

ax.legend()
ax.set_title("AoC_prop at sea level")

plt.show()

################################################################################################################################





#Angle of climb at 2000 m 
 
hG = 2000 

T,P,rho = eval_T_P_rho(2000, h_flag="hG") 
rho_h_1_p = rho 
 
P_av_0_prop = 171510.977*0.8
P_av_1_prop = ((rho_h_1_p/rho_sl)-((1-(rho_h_1_p/rho_sl))/7.55))*P_av_0_prop 
 
V_prop_T_1 = numpy.linspace(9, 75,1000) 
 
a_T_prop_1 = (rho_h_1_p*S_prop*cd_0_prop)/2 
b_T_prop_1 = (2*k_prop*S_prop)/rho_h_1_p 
c_T_prop_1 = (numpy.power((W_prop/S_prop),2)) 
 

T_av_1_prop = P_av_1_prop/V_prop_T_1 
T_req_prop_1 = (a_T_prop_1*numpy.power(V_prop_T_1,2))+((b_T_prop_1*c_T_prop_1)*(1/(numpy.power(V_prop_T_1,2)))) 
P_req_prop_1 = T_req_prop_1*V_prop_T_1 
 
AoC_1_prop = ((P_av_1_prop-P_req_prop_1)/(W_prop*V_prop_T_1))*(180/math.pi)
 
fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_prop_T_1,AoC_1_prop, label = "AoC_prop_2000m") 
 
ax.set_xlabel("V_prop") 
ax.set_ylabel("AoC_prop_2000m") 
 
ax.legend() 
ax.set_title("AoC_prop at 2000m") 
 
plt.show() 

#####################################################################################################################################

hG = 4000 
T,P,rho = eval_T_P_rho(4000, h_flag="hG") 
rho_h_2_p = rho 
 
P_av_0_prop = 171510.977*0.8
P_av_2_prop = ((rho_h_2_p/rho_sl)-((1-(rho_h_2_p/rho_sl))/7.55))*P_av_0_prop 
 
V_prop_T_2 = numpy.linspace(13, 72,1000) 
 
a_T_prop_2 = (rho_h_2_p*S_prop*cd_0_prop)/2 
b_T_prop_2 = (2*k_prop*S_prop)/rho_h_2_p 
c_T_prop_2 = (numpy.power((W_prop/S_prop),2)) 
 

T_av_2_prop = P_av_2_prop/V_prop_T_2 
T_req_prop_2 = (a_T_prop_2*numpy.power(V_prop_T_2,2))+((b_T_prop_2*c_T_prop_2)*(1/(numpy.power(V_prop_T_2,2)))) 
P_req_prop_2 = T_req_prop_2*V_prop_T_2 
 
AoC_2_prop = ((P_av_2_prop-P_req_prop_2)/(W_prop*V_prop_T_2))*(180/math.pi) 
 
fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_prop_T_2,AoC_2_prop, label = "AoC_prop_4000m") 
 
ax.set_xlabel("V_prop") 
ax.set_ylabel("AoC_prop_4000m") 
 
ax.legend() 
ax.set_title("AoC_prop at 4000m") 
 
#plt.show() 

#####################################################################################################################################

fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_prop_T,AoC_0_prop, label = "AoC_prop_0m") 
ax.plot(V_prop_T,AoC_1_prop, label = "AoC_prop_2000m") 
ax.plot(V_prop_T,AoC_2_prop, label = "AoC_prop_4000m") 
 
ax.set_xlabel("V_prop") 
ax.set_ylabel("AoC_prop") 
 
ax.legend() 
ax.set_title("AoC_prop(h)") 
 
plt.show() 

#########################################################################################################################################


#Rate of climb prop at sea level 
 
hG = 0 

 
T_av_0_prop = P_av_0_prop/V_prop_T 
T_req_prop = (a_T_prop*numpy.power(V_prop_T,2))+((b_T_prop*c_T_prop)*(1/(numpy.power(V_prop_T,2)))) 
P_req_prop = T_req_prop*V_prop_T 
 
RoC_0_prop = (P_av_0_prop-P_req_prop)/(W_prop) 
 
fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_prop_T,RoC_0_prop, label = "RoC_prop_0m") 
 
ax.set_xlabel("V_prop") 
ax.set_ylabel("RoC_prop_0m") 
 
ax.legend() 
ax.set_title("RoC_prop at sea level") 
 
plt.show() 

####################################################################################################################################

#Rate of climb at 2000 m 
 
hG = 2000 

T,P,rho = eval_T_P_rho(2000, h_flag="hG") 
rho_h_1_p = rho 
 

P_av_1_prop = ((rho_h_1_p/rho_sl)-((1-(rho_h_1_p/rho_sl))/7.55))*P_av_0_prop 
  

T_av_1_prop = P_av_1_prop/V_prop_T_1 
T_req_prop_1 = (a_T_prop_1*numpy.power(V_prop_T_1,2))+((b_T_prop_1*c_T_prop_1)*(1/(numpy.power(V_prop_T_1,2)))) 
P_req_prop_1 = T_req_prop_1*V_prop_T_1 
 
RoC_1_prop = (P_av_1_prop-P_req_prop_1)/(W_prop) 
 
fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_prop_T_1,RoC_1_prop, label = "RoC_prop_2000m") 
 
ax.set_xlabel("V_prop") 
ax.set_ylabel("RoC_prop_2000m") 
 
ax.legend() 
ax.set_title("RoC_prop at 2000m") 
 
plt.show() 

#########################################################################################################################################

#Rate of climb at 4000 
 
hG = 4000 

T,P,rho = eval_T_P_rho(4000, h_flag="hG") 
rho_h_2_p = rho 
 
 
P_av_2_prop = ((rho_h_2_p/rho_sl)-((1-(rho_h_2_p/rho_sl))/7.55))*P_av_0_prop 
 
T_av_2_prop = P_av_2_prop/V_prop_T_2 
T_req_prop_2 = (a_T_prop_2*numpy.power(V_prop_T_2,2))+((b_T_prop_2*c_T_prop_2)*(1/(numpy.power(V_prop_T_2,2)))) 
P_req_prop_2 = T_req_prop_2*V_prop_T_2 
 
RoC_2_prop = (P_av_2_prop-P_req_prop_2)/(W_prop) 
 
fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_prop_T_2,RoC_2_prop, label = "RoC_prop_4000m") 
 
ax.set_xlabel("V_prop") 
ax.set_ylabel("RoC_prop_4000m") 
 
ax.legend() 
ax.set_title("RoC_prop at 4000m") 
 
#plt.show() 

############################################################################################################################## 

fig = plt.figure() 
ax = fig.gca() 
 
ax.plot(V_prop_T,RoC_0_prop, label = "RoC_prop_0m") 
ax.plot(V_prop_T_1,RoC_1_prop, label = "RoC_prop_2000m") 
ax.plot(V_prop_T_2,RoC_2_prop, label = "RoC_prop_4000m") 
 
ax.set_xlabel("V_prop") 
ax.set_ylabel("RoC_prop") 
 
ax.legend() 
ax.set_title("RoC_prop(h)") 
 
plt.show()

######################################################################################################################################


# PUNTO 2 ##########################################

h = numpy.linspace(0, 4000, 100)

dt_under_dh_0 = numpy.zeros_like(h)

for i in range(len(h)):
    
    T, p, rho = eval_T_P_rho(h[i])
    
    W_prop = 1133.98*9.81
    
    a_T_prop = (rho*S_prop*cd_0_prop)/2 
    b_T_prop = (2*k_prop*S_prop)/rho
    c_T_prop = (numpy.power((W_prop/S_prop), 2)) 
    
    V_prop = (numpy.power((2*W_prop)/(rho*S_prop), 1/2)*numpy.power(k_prop/cd_0_prop, 1/4))*0.76
    
    P_av_0_prop = 171510.977*0.8
    P_av_prop = ((rho/rho_sl)-((1-(rho/rho_sl))/7.55))*P_av_0_prop
    
    T_req_prop = (a_T_prop*numpy.power(V_prop, 2))+((b_T_prop*c_T_prop)*(1/(numpy.power(V_prop,2)))) 
    P_req_prop = T_req_prop*V_prop
    
    dt_under_dh_0[i] = W_prop/(P_av_prop-P_req_prop)
    
    if dt_under_dh_0[i] <= 0:
        
        dt_under_dh_0[i] = numpy.nan
    

'TIME OF CLIMB'

t_of_climb = 0

for i in range(len(h)):
    if str(dt_under_dh_0[i]) == "nan":
        break
    else:
        if i == 0: 
            t_of_climb += dt_under_dh_0[i] * h[i]
        else:
            t_of_climb += dt_under_dh_0[i] * (h[i]-h[i-1])
       
print("\n\nTime of climb at constant attitude for propeller is: " + str(t_of_climb /60) + " minutes")



h_array = numpy.linspace(0, 4000, 100)


    
dt_under_dh = numpy.zeros_like(h_array)

for i in range(len(h_array)):
    
    T, p, rho = eval_T_P_rho(h_array[i])
    
    W_prop = 1133.98*9.81
    
    a_T_prop = (rho*S_prop*cd_0_prop)/2 
    b_T_prop = (2*k_prop*S_prop)/rho
    c_T_prop = (numpy.power((W_prop/S_prop), 2)) 
    
    V_prop = 50
    
    P_av_0_prop = 171510.977*0.8
    P_av_prop = ((rho/rho_sl)-((1-(rho/rho_sl))/7.55))*P_av_0_prop
    
    T_req_prop = (a_T_prop*numpy.power(V_prop, 2))+((b_T_prop*c_T_prop)*(1/(numpy.power(V_prop,2)))) 
    P_req_prop = T_req_prop*V_prop
    
    dt_under_dh[i] = W_prop/(P_av_prop-P_req_prop)
    
    if dt_under_dh[i] <= 0:
        
        dt_under_dh[i] = numpy.nan


fig = plt.figure()
ax = fig.gca()
ax.plot(h_array, dt_under_dh, marker = ",", color = "red", label = "dt/dh for const speed")
ax.plot(h_array,dt_under_dh_0 , marker = ",", color = "cyan", label = "dt/dh for const attitude")
ax.set_title("dt/dh as function of altitude _ prop")
ax.set_xlabel("dt/dh")
ax.set_ylabel("altitude")
plt.legend()
plt.show()      
        
'TIME OF CLIMB'

t_of_climb = 0

for i in range(len(h_array)):
    if str(dt_under_dh[i]) == "nan":
        break
    else:
        if i == 0: 
            t_of_climb += dt_under_dh[i] * (h_array[i]-h_array[i])
        else:
            t_of_climb += dt_under_dh[i] * (h_array[i]-h_array[i-1])
       
print("\n\nTime of climb at constant speed for propeller is: " + str(t_of_climb /60) + " minutes")       

# JET ############################################################

h = numpy.linspace(0, 6705, 100)

dt_under_dh_0 = numpy.zeros_like(h)

for i in range(len(h)):
    
    T, p, rho = eval_T_P_rho(h[i])
    
    a_T_jet_0 = (rho*S_jet*cd_0_jet)/2 
    b_T_jet_0 = (2*k_jet*S_jet)/rho
    c_T_jet_0 = (numpy.power((W_jet/S_jet),2))
    
    S_jet = 48.96 
    cd_0_jet = 0.02 
    lambda_jet = (19.38*19.38)/(48.96) 
    k_jet = 1/(math.pi*0.81*lambda_jet) 
    W_jet = 16193.248*9.81 
    T_av_0 = 30087.77109348909*2
    
    a = T_av_0/rho_sl
    b = 12*cd_0_jet*k_jet*W_jet
    d = S_jet*cd_0_jet/2
    
    V_ROC_max_jet = numpy.power((a*rho + numpy.power(((a*rho)**2) + b, 1/2))/(6*d*rho),1/2)
    
    T_av = (rho/rho_sl)*T_av_0 
    P_av_jet = T_av*V_ROC_max_jet
    
    T_req_jet = (a_T_jet_0*numpy.power(V_ROC_max_jet,2))+((b_T_jet_0*c_T_jet_0)*(1/(numpy.power(V_ROC_max_jet,2)))) 
    P_req_jet = V_ROC_max_jet*T_req_jet
   
    
    dt_under_dh_0[i] = W_jet/(P_av_jet-P_req_jet)
    
    if dt_under_dh_0[i] <= 0:
        
        dt_under_dh_0[i] = numpy.nan  
        

'TIME OF CLIMB'

t_of_climb = 0

for i in range(len(h)):
    if str(dt_under_dh[i]) == "nan":
        break
    else:
        if i == 0: 
            t_of_climb += dt_under_dh_0[i] * h[i]
        else:
            t_of_climb += dt_under_dh_0[i] * (h[i]-h[i-1])
       
print("\n\nTime of climb at constant attitude for jet is: " + str(t_of_climb /60) + " minutes")


h_array = numpy.linspace(0, 6705, 100)
Vmax = numpy.zeros_like(h_array)

for k in range(0, len(h_array), 1):
    
    T_k, p_k, rho = eval_T_P_rho(h_array[k])
    
    a_T_jet_h = (rho*S_jet*cd_0_jet)/2 
    b_T_jet_h = (2*k_jet*S_jet)/rho
    c_T_jet_h = (numpy.power((W_jet/S_jet),2)) 
    
    T_max_sl = 2*30087.77109348909
    
    T_av = (rho/rho_sl)*T_max_sl
    
    Vmax[k] = numpy.power((T_av/(2*a_T_jet_h))*(1+numpy.power(1-((4*a_T_jet_h*b_T_jet_h*c_T_jet_h)/(T_av**2)), 1/2)), 1/2)
  
dt_under_dh_1 = numpy.zeros_like(h_array)

for i in range(len(h_array)):
    
    T, p, rho = eval_T_P_rho(h_array[i])
    S_jet = 48.96 
    cd_0_jet = 0.02 
    lambda_jet = (19.38*19.38)/(48.96) 
    k_jet = 1/(math.pi*0.81*lambda_jet) 
    W_jet = 16193.248*9.81 
    T_av_0 = 30087.77109348909*2
    
    a_T_jet_0 = (rho*S_jet*cd_0_jet)/2 
    b_T_jet_0 = (2*k_jet*S_jet)/rho
    c_T_jet_0 = (numpy.power((W_jet/S_jet),2))
    
    V_jet =  112.59273693803792
    
    T_av = (rho/rho_sl)*T_av_0 
    P_av_jet = T_av*V_jet
    
    T_req_jet = (a_T_jet_0*numpy.power(V_jet, 2))+((b_T_jet_0*c_T_jet_0)*(1/(numpy.power(V_jet, 2)))) 
    P_req_jet = V_jet*T_req_jet
   
    
    dt_under_dh_1[i] = W_jet/(P_av_jet-P_req_jet)
    
    if dt_under_dh_1[i] <= 0:
        
        dt_under_dh_1[i] = numpy.nan

fig = plt.figure()
ax = fig.gca()
ax.plot(h_array, dt_under_dh_1, marker = ",", color = "brown", label = "dt/dh_const_speed")
ax.plot(h, dt_under_dh_0, marker = ",", color = "cyan", label = "dt/dh const_attitude")
ax.set_title("dt/dh as function of altitude _ jet")
ax.set_xlabel("dt/dh")
ax.set_ylabel("altitude")
plt.legend()
plt.show()

'TIME OF CLIMB'

t_of_climb = 0

for i in range(len(h)):
    if str(dt_under_dh[i]) == "nan":
        break
    else:
        if i == 0: 
            t_of_climb += dt_under_dh_1[i] * h_array[i]
        else:
            t_of_climb += dt_under_dh_1[i] * (h_array[i]-h_array[i-1])
            
       
print("\n\nTime of climb at constant speed for jet is: " + str(t_of_climb /60) + " minutes")

