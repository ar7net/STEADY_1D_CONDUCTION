import numpy as np
import matplotlib.pyplot as plt

L=0.05
n=20
dx=L/(n-1)
x=np.linspace(0,L,n)
T=np.array(np.zeros(n))
e=600000
k=28
h=60
T_amb=30
tol=0.0001
error=1
iter=0

while error>tol:
    Told=np.copy(T)
    T[0]=Told[1]+(e*dx**2)/(2*k) 
    T[-1]=(h*T_amb+(k*Told[n-2]/dx)+(e*dx/2))/(h+(k/dx))
    
    for i in range(1,n-1):
        T[i]=0.5*(Told[i-1]+Told[i+1]+(e*dx**2/k))
    error=np.max(np.abs(np.array(Told-T)))
    iter=iter+1
    
# GRAFICO 
from matplotlib.pyplot import figure
plt.style.use("dark_background")
figure(figsize=(10,6))
plt.plot(x,T, linewidth=4)
plt.title("Variación de la Temperatura", fontsize=18)
plt.xlim(0,L)
plt.ylim(530,557)
plt.xlabel("Longitud (m)", fontsize=18)
plt.ylabel("Temperatura (°C)", fontsize=18)
plt.grid(linestyle=":", linewidth=0.5)
plt.show()

#RESULTADOS 

import pandas as pd
df = pd.DataFrame({"x (m)": x, "Temperatura (°C)": T})
pd.options.display.float_format = "{:,.2f}".format
print(df)
