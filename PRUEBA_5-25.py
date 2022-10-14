import numpy as np
import matplotlib.pyplot as plt

L=0.05
n=6
dx=L/(n-1)
dx=np.linspace(0, L, n)

k=180
h=25
T_amb=25
T_alr=290  # Kelvin
TL=180
e=0.9
b=0.01
w=1

tan_theta=b/(2*L)
theta=np.arctan(tan_theta)*180/np.pi
cos_theta=np.cos(theta*np.pi/180)
sigma=5.67*10**(-8)

C3=h*(2*w*dx)/cos_theta
C4=e*sigma*2*w/cos_theta
C5=k*tan_theta
C6=(2*h*(dx/2))/cos_theta
C7=(2*e*sigma*(dx/2))/cos_theta


T=np.array(np.zeros(n))
T[0]=TL
tol=0.00001
error=1.
iter=2

a=iter**4
print(a)

while error>tol:
    Told=np.copy(T)
    T[-1]=(C5*Told[n-2]+C6*T_amb+C7*((T_alr**4)-(Told[-1]+273)**4))/(C5+C6)
     
    
    for i in range(1, n-1):
        C1=k*2*w*(L-(i-0.5)*dx)*tan_theta
        C2=k*2*w*(L-(i+0.5)*dx)*tan_theta
        
        T[i]=((C1/dx)*T[i-1]+(C2/dx)*T[i+1]+C3*T_amb+C4*(T_alr**4-(Told[i]+273)**4)/((C1/dx)+(C2/dx)+C3))
        
              
    error=np.max(np.abs(np.array(T-Told)))                            
    iter=iter+1
        
        
        
        
        
    

    
