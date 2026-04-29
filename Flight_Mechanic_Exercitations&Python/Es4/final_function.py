import math
import numpy as np

while True:
    
    p = input("Choose weight or velocity:\n")
    
    if p == "velocity":
    
        a = input("input the frame for velocity:\n")
        print("azimuth angle of velocity is equal to sideslip angle")  
        v = 223.52
        V_vector = [v, 0, 0]
        
        if a == "aerodynamic":
            
            psi = -1
            theta = 0
            phi = 0
            
            R_psi = np.array([[math.cos(math.radians(psi)),-math.sin(math.radians(psi)),0],[math.sin(math.radians(psi)), math.cos(math.radians(psi)), 0 ],[0, 0, 1]])
        
            R_theta = np.array([[math.cos(math.radians(theta)),0 ,math.sin(math.radians(theta))],[0, 1, 0 ],[-math.sin(math.radians(theta)), 0, math.cos(math.radians(theta))]])
        
            R_phi = np.array([[1, 0, 0],[0, math.cos(math.radians(phi)), -math.sin(math.radians(phi)) ],[0, math.sin(math.radians(phi)), math.cos(math.radians(phi))]])
            
            R_res = np.dot(R_psi, R_theta, R_phi)
        
            V_frame = np.dot(V_vector, R_res)
        
            print(f"\nVelocity in aerodynamic frame is:\n\n {V_frame}")
            
            
        elif a == "body":
            
            psi = -1
            theta = 5
            phi = 0
            
            R_psi = np.array([[math.cos(math.radians(psi)),-math.sin(math.radians(psi)),0],[math.sin(math.radians(psi)), math.cos(math.radians(psi)), 0 ],[0, 0, 1]])
        
            R_theta = np.array([[math.cos(math.radians(theta)),0 ,math.sin(math.radians(theta))],[0, 1, 0 ],[-math.sin(math.radians(theta)), 0, math.cos(math.radians(theta))]])
        
            R_phi = np.array([[1, 0, 0],[0, math.cos(math.radians(phi)), -math.sin(math.radians(phi)) ],[0, math.sin(math.radians(phi)), math.cos(math.radians(phi))]])
            
            R_res = np.dot(R_psi, R_theta, R_phi)
        
            V_frame = np.dot(V_vector, R_res)
            
            print(f"\nVelocity in body frame is:\n\n {V_frame}")
            
        
        elif a == "vertical":
            
            psi = -1
            theta = 5-10
            phi = -20  
            
            R_psi = np.array([[math.cos(math.radians(psi)),-math.sin(math.radians(psi)),0],[math.sin(math.radians(psi)), math.cos(math.radians(psi)), 0 ],[0, 0, 1]])
        
            R_theta = np.array([[math.cos(math.radians(theta)),0 ,math.sin(math.radians(theta))],[0, 1, 0 ],[-math.sin(math.radians(theta)), 0, math.cos(math.radians(theta))]])
        
            R_phi = np.array([[1, 0, 0],[0, math.cos(math.radians(phi)), -math.sin(math.radians(phi)) ],[0, math.sin(math.radians(phi)), math.cos(math.radians(phi))]])
            
            R_res = np.dot(R_psi, R_theta, R_phi)
        
            V_frame = np.dot(V_vector, R_res)
            
            glide_angle = 10-5
            
            print(f"Velocity in vertical frame is:\n\n {V_frame}")
            print(f"Glide angle is:\n\n {glide_angle}")
        
        else:
            
            print("\ninvalid input")
            
            
    elif p == "weight": 
        
        b = input("\ninput the frame for weight:\n")
        w = 4581.2829
        W_vector = [0, 0, w]
    
        if b == "body":
            
            psi = 0
            theta = -10  
            phi = -20    
            
            R_psi = np.array([[math.cos(math.radians(psi)),-math.sin(math.radians(psi)),0],[math.sin(math.radians(psi)), math.cos(math.radians(psi)), 0 ],[0, 0, 1]])
        
            R_theta = np.array([[math.cos(math.radians(theta)),0 ,math.sin(math.radians(theta))],[0, 1, 0 ],[-math.sin(math.radians(theta)), 0, math.cos(math.radians(theta))]])
        
            R_phi = np.array([[1, 0, 0],[0, math.cos(math.radians(phi)), -math.sin(math.radians(phi)) ],[0, math.sin(math.radians(phi)), math.cos(math.radians(phi))]])
            
            R_res = np.dot(R_psi, R_theta, R_phi)
        
            W_frame = np.dot(W_vector, R_res)
            
            print(f"\nWeight in body frame is:\n\n {W_frame}")
            
            
        elif b == "wind":
            
            psi = 1  
            theta = 5
            phi = 20  
             
            R_psi = np.array([[math.cos(math.radians(psi)),-math.sin(math.radians(psi)),0],[math.sin(math.radians(psi)), math.cos(math.radians(psi)), 0 ],[0, 0, 1]])
        
            R_theta = np.array([[math.cos(math.radians(theta)),0 ,math.sin(math.radians(theta))],[0, 1, 0 ],[-math.sin(math.radians(theta)), 0, math.cos(math.radians(theta))]])
        
            R_phi = np.array([[1, 0, 0],[0, math.cos(math.radians(phi)), -math.sin(math.radians(phi)) ],[0, math.sin(math.radians(phi)), math.cos(math.radians(phi))]])
            
            R_res = np.dot(R_psi, R_theta, R_phi)
        
            W_frame = np.dot(W_vector, R_res)
            
            print(f"\nWeight in wind frame is:\n\n {W_frame}")
            

      
           