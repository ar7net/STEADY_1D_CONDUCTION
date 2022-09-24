# PASO 1: Inicializar
import numpy as np   
import matplotlib.pyplot as plt  
plt.style.use('dark_background')

# PASO 2:  Construir malla unidimensional
L=0.05
n=6
dx=L/(n-1)
x=np.linspace(0,L,n)
b=0.01
w=1
tan_theta=(b/2)/L
theta=np.arctan(tan_theta)*180/np.pi
cos_theta=np.cos(theta*np.pi/180)
 
# PASO 3: Propiedades termofísicas
T_amb=25
h=15
k=180
C=(h*2*w*dx)/cos_theta
E=(h*2*w*dx/2)/cos_theta
D=(k*2*w*dx/2)*tan_theta

# PASO 4: Condiciones de frontera
T=np.array(np.zeros(n))
TL=200
T[0]=TL

# PASO 5: Criterio de convergencia
err=1.
tol=0.0001
iter=0

# PASO 6: Diferencias finitas, iteración de Jacobi
while (err>tol):
    Told=np.array(T)
    T[-1]= ((D/dx)*T[n-2] + E*T_amb) / ((D/dx)+E)
    for i in range(1,n-1):
        A=2*k*w*(L-(i-0.5)*dx)*tan_theta
        B=2*k*w*(L-(i+0.5)*dx)*tan_theta
        T[i]=(((A/dx)*Told[i-1]+(B/dx)*Told[i+1]+C*T_amb)
              /((A/dx)+(B/dx)+C))
    err=np.amax(np.abs(np.array(Told-T)))
    iter=iter+1
       
# PASO 7: Resultados
np.set_printoptions(precision=1)
print(T)

# PASO 8: Grafico
from matplotlib.pyplot import figure
figure(figsize=(10,6))
plt.plot(x,T, linewidth=3)
plt.title('Variación de T vs X', fontsize=18)
plt.xlim(0,L)
plt.ylim(192,200)
plt.xlabel("Longitud [m]", fontsize=18)
plt.ylabel("Temperatura de la pared [°C]", fontsize=18)
plt.grid(linestyle=":", linewidth=0.5)
plt.show()