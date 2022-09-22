import numpy as np
import matplotlib.pyplot as plt

# DATOS DE ENTRADA (PROBLEMA EJEMPLO 5-1, CENGEL, pag 297)

L=0.04                      # Longitud de la pared [m]              
n=3                         # Número de nodos
dx=L/(n-1)                  # Delta X [m]
x=np.linspace(0,L,n)        # Malla unidimensional para la pared
T=np.array(np.zeros(n))     # Crear el array de temperatura


T_amb=30                    # Temperatura ambiente [°C]
h=45                        # Coeficiente de convección [W/m^2K]
q=5000000                   # Generación de calor [W/m^3]
k=28                        # Conductividad térmica [W/mK]


# CONDICIONES DE FRONTERA
TL=0                        # Condición de frontera izquierda
T[0]=TL                     # Fijar la condición de frontera izquierda

# CRITERIO DE CONVERGENCIA, ERROR Y CONTADOR
err=1.                      # Inicializar error
tol=0.00001                 # Definir la tolerancia
iter=0.0                    # Inicializar contador

# SOLVER - ITERACIÓN DE DIFERENCIAS FINITAS (MÉTODO JACOBI)

while (err>tol):
    Told=np.array(T)
    T[n-1]=(h*T_amb+(k*Told[n-2]/dx)+(q*dx/2))/(h+(k/dx))   # Condición de frontera de convección pared derecha.
  
    for i in range(1, n-1):
        T[i]=0.5*(Told[i-1]+Told[i+1]+((q*dx**2)/k))    # Nodos interiores
  
    err=np.amax(np.abs(np.array(Told-T)))
    iter=iter+1

print("El valor de las teperatura T2 = ", T[1])

# GRÁFICOS
plt.plot(x,T)
plt.show()


	

