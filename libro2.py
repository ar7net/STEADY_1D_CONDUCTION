import numpy as np

def tripiv(a, b, c, d):
    """Solution of a linear system of algebraic equations with a
        tri-diagonal matrix of coefficients using the Thomas-algorithm with pivoting.

    Args:
        a(array): an array containing lower diagonal (a[0] is not used)
        b(array): an array containing main diagonal 
        c(array): an array containing lower diagonal (c[-1] is not used)
        d(array): right hand side of the system
    Returns:
        x(array): solution array of the system
    
    """
    
    n = len(b)
    x = np.zeros(n)
    fail = 0
    
    # reordering
    
    a[0] = b[0]
    b[0] = c[0]
    c[0] = 0
    
    # elimination:
    
    l = 0
    
    for k in range(0,n):
        q = a[k]
        i = k
        
        if l < n-1:
            l = l + 1
    
        for j in range(k+1,l+1):
            q1 = a[j]
            if (np.abs(q1) > np.abs(q)):
                q = q1
                i = j
        if q == 0:
            fail = -1
        
        if i != k:
            q = d[k]
            d[k] = d[i]
            d[i] = q
            q = a[k]
            a[k] = a[i]
            a[i] = q
            q = b[k]
            b[k] = b[i]
            b[i] = q
            q = c[k]
            c[k] =c[i]
            c[i] = q
        for i in range(k+1,l+1):
            q = a[i]/a[k]
            d[i] = d[i]-q*d[k]
            a[i] = b[i]-q*b[k]
            b[i] = c[i]-q*c[k]
            c[i] = 0
            

    
    # backsubstitution
    
    x[n-1] = d[n-1]/a[n-1]
    x[n-2] = (d[n-2]-b[n-2]*x[n-1])/a[n-2]
    
    for i in range(n-3,-1,-1):
        
        q = d[i] - b[i]*x[i+1]
        x[i] = (q - c[i]*x[i+2])/a[i]
    
    return x


a = [0,0,0.5,0.5,0.5]
b = [1,-1,-1,-1,1]
c = [0.5,0.5,0.5,0,0 ]
d = [0,0,0,0,100]

# Call thomas function
x = tripiv(a,b,c,d)
print(x)