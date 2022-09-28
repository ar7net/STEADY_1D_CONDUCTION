import numpy as np
import matplotlib.pyplot as plt

L=1
n=9
dx=L/(n-1)
x=np.linspace(0,L,n)

T=np.array(np.zeros(n))
TL=30
T[0]=TL
k=45
q=1200

tol=0.0001
error=1
iter=0

while error>tol:
    Told=np.copy(T)
    T[-1]=Told[n-2]+q/(k/dx)
    
    for i in range(1,n-1):
        T[i]=0.5*(Told[i-1]+Told[i+1])
    error=np.max(np.abs(np.array(Told-T)))
    iter=iter+1
    
np.set_printoptions(precision=2)
print("El vector de Temperaturas es:\n")
print(T)
print("\nNúmero de iteraciones: ", iter)

from matplotlib.pyplot import figure
plt.style.use("dark_background")
figure(figsize=(10,6))
plt.plot(x,T, linewidth=3)
plt.title("Variación de la Temperatura", fontsize=18)
plt.xlim(0,L)
plt.ylim(30,60)
plt.xlabel("Longitud (m)", fontsize=18)
plt.ylabel("Temperatura (°C)", fontsize=18)
plt.grid(linestyle=":", linewidth=0.5)
plt.show()