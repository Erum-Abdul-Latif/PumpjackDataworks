import cmath
######### Basit Code Part
def slope_formula(x11,x22,y11,y22):
    gradient= (y22-y11)/(x22-x11)
    return gradient
#########

####### mustafain

def slope_formulaa(a,b):
    c=math.pow(a+b,2)
    return c
############

####Abdul-Rehman###
# -*- coding: utf-8 -*-
"""Untitled1.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1_-9q1Ri72xPEd3BZidwv3iGgSHKWQ3Ir
**Importing Files.**
"""

import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

"""**Initialization**
"""

P=3; # period value to integrate continous value between [0,3]
BT=-6 # INTIAL TIME TO START THE SERIES
ET=6 # FINAL TIME
FS=1000 # NO OF DISCRETE VALUES TO BE GENERATED

"""Let t be an independent varaible.
f(t)=((tmodP)−(P/2))**3 , with period P=3
"""

f = lambda t: ((t % P) - (P / 2.)) ** 3

"""Discrete values of t between bt and ET
"""

t_range = np.linspace(BT, ET, FS)
y_true = f(t_range) #the true f(t)

"""function that computes the real fourier couples of coefficients (a0, 0), (a1, b1)...(aN, bN)"""

def compute_real_fourier_coeffs(func, N):
    result = []
    for n in range(N+1):
        an = (2./P) * spi.quad(lambda t: func(t) * np.cos(2 * np.pi * n * t / P), 0, P)[0]
        bn = (2./P) * spi.quad(lambda t: func(t) * np.sin(2 * np.pi * n * t / P), 0, P)[0]
        result.append((an, bn))
    return np.array(result)

"""function that computes the real form Fourier series using an and bn coefficients"""

def fit_func_by_fourier_series_with_real_coeffs(t, AB):
    result = 0.
    A = AB[:,0]
    B = AB[:,1]
    for n in range(0, len(AB)):
        if n > 0:
            result +=  A[n] * np.cos(2. * np.pi * n * t / P) + B[n] * np.sin(2. * np.pi * n * t / P)
        else:
            result +=  A[0]/2.
    return result

"""**Plotting graph**"""

def plot_graph():
  P=input("Enter Period for fourier Series:")
  maxN=8
  COLs = 2 #cols of plt
  ROWs = 1 + (maxN-1) // COLs #rows of plt
  plt.rcParams['font.size'] = 8
  fig, axs = plt.subplots(ROWs, COLs)
  fig.tight_layout(rect=[0, 0, 1, 0.95], pad=3.0)
  fig.suptitle('f(t) = ((t % P) - (P / 2.)) ** 3 where P=' + str(P))

  #plot, in the range from BT to ET, the true f(t) in blue and the approximation in red
  for N in range(1, maxN + 1):
      AB = compute_real_fourier_coeffs(f, N)
      #AB contains the list of couples of (an, bn) coefficients for n in 1..N interval.

      y_approx = fit_func_by_fourier_series_with_real_coeffs(t_range, AB)
      #y_approx contains the discrete values of approximation obtained by the Fourier series

      row = (N-1) // COLs
      col = (N-1) % COLs
      axs[row, col].set_title('case N=' + str(N))
      axs[row, col].scatter(t_range, y_true, color='blue', s=1, marker='.')
      axs[row, col].scatter(t_range, y_approx, color='red', s=2, marker='.')
  plt.show()

###################
import numpy, math
import sys
def relax(A, maxsteps, convergence):
    iterations = 0
    diff = convergence +1

    Nx = A.shape[1]
    Ny = A.shape[0]
    
    while iterations < maxsteps and diff > convergence:
        Atemp = A.copy()
        diff = 0.0
        
        for y in range(1,Ny-1):
            for x in range(1,Ny-1):
                A[y,x] = 0.25*(Atemp[y,x+1]+Atemp[y,x-1]+Atemp[y+1,x]+Atemp[y-1,x])
                diff  += math.fabs(A[y,x] - Atemp[y,x])

        diff /=(Nx*Ny)
        iterations += 1
    print ("Output : ", diff)

def boundary(A,x,y):


    Nx = A.shape[1]
    Ny = A.shape[0]
    Lx = x[Nx-1] 
    Ly = x[Nx-1]


    A[:,0]    =   100*numpy.sin(math.pi*x/Lx)
    A[:,Nx-1] = - 100*numpy.sin(math.pi*x/Lx)
    A[0,:]    = 0.0
    A[Ny-1,:] = 0.0

def fourierseries():
    plot_graph();
def slopeformula1():
    x1=float(input("Enter the first xcoordinate:"))
    x2=float(input("Enter the second xcoordinate:"))
    y1=float(input("Enter the first ycoordinate:"))
    y2=float(input("Enter the second ycoordinate:"))
    Output=slope_formula(x1,x2,y1,y2)
    print("The slope of the given formula is:",Output)

def slopeformula2():
    import math
    n1=input('Enter First Number : ')
    n2=input('Enter Second Number : ')
    n1 = float(n1)
    n2 = float(n2)
    print(slope_formulaa(n1,n2))

    
def quadraticformula():
    a = float(input('Enter a: '))  
    b = float(input('Enter b: '))  
    c = float(input('Enter c: '))  
 
    determinant = (b**2) - (4*a*c)  

    if determinant > 0:
        root1 = (-b-cmath.sqrt(determinant))/(2*a) 
        root2 = (-b+cmath.sqrt(determinant))/(2*a) 

        print('root1 = {0} and root2 = {1}'.format(root1,root2))

    elif determinant == 0:
        root1 = root2 = -b / (2 * a)
        print('root1 = root2 =', root1)

    else:
        real = -b/(2*a)
        imaginary = cmath.sqrt(-determinant)/(2*a)
        print('root1 = {0}+{1}i'.format(real,imaginary))
        print('root2 = {0}+{1}i'.format(real,imaginary))
        
def laplaceformula():
    Nx = input("Enter Nx : ")
    Ny = input("Enter Ny : ")
    if Nx!=Ny:
        print("Nx and Ny must be equal")
        exit()
    maxiter = input("Enter no of iterations (P) : ")
    Nx=int(Nx)
    Ny=int(Ny)
    maxiter=int(maxiter)

    x = numpy.linspace(0,1,num=Nx+2)
    y = numpy.linspace(0,1,num=Ny+2)
    A = numpy.zeros((Nx+2,Ny+2))

    boundary(A,x,y)
    relax(A,maxiter,0.00001)
    # return "friday"
def default():
    return "Invalid choice"

switcher = {
    1: fourierseries,
    2: slopeformula1,
    3: slopeformula2,
    4: quadraticformula,
    5: laplaceformula
    }
  
def switch(formula):
    return switcher.get(formula, default)()

if __name__ == "__main__":
    formula = float(input('Enter choice: '))
    switch(formula)