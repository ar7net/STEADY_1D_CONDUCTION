import numpy as np

#conducción 1D estado estable. Temperaturas fijas en extremos, sin generación

TL=10
TR=100
nodos=6

a=np.zeros(nodos)
b=np.zeros(nodos)
d=np.zeros(nodos)

# ensamblar [a] y [c]
a[0]=0
a[-1]=0

for i in range(1,nodos-1):
    a[i]=0.5

c=np.copy(a)


# ensamblar [b] diagonal principal

b[0]=1
b[-1]=1

for i in range(1, nodos-1):
    b[i]=-1


# ensamblar vector de términos del lado derecho
d[0]=TL
d[-1]=TR

for i in range(1, nodos-1):
    d[i]=0

print(a)
print(b)
print(c)
print(d)






