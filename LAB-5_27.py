# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:11:22 2022

@author: cb.en.u4cce19027
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath

# Function to Plot
def fplot(t,x):
    plt.stem(x)
    plt.title(t)
    plt.xlabel('SAMPLES')
    plt.ylabel('AMPLITUDE')
    plt.show()

def main():
    u=[1 for i in range(10)] # generating signal for u[n]
    u3 =[0 if i<3 else 1 for i in range(10)] # generating signal for u[n-3]
    
    h=[u3[i]-u[i] for i in range(10)]  # generating signal for u[n-3] - u[n]
    h1=[h[i]*(0.5)**i for i in range(len(h))] # generating signal for (u[n-3]- u[n])*0.5
    
    fplot("Plot for u[n]",u) # Plotting U[n]
    fplot("Plot for u[n-3]",u3) # Plottng U[n-3]
    fplot("Plot for u[n-3]- u[n]",h) # Plottng U[n-3] - u[n]
    fplot("Plot for (u[n-3]- u[n])*0.5 (impulse response)", h1) #Plotting (u[n-3]- u[n])*0.5 (Impulse response)
    
    H=[]
    for i in range(len(h1)):
        s=0
        for k in range(len(h1)):
            s+=h1[k]*np.exp(-1j*i*k)
        H.append(s) 
    
    magnitude=[abs(H[i]) for i in range(len(H))]  # Geting the Magnitude response
    
    plt.stem(magnitude)  # Plotting Magnitude Response
    plt.xlabel('FREQUENCY')
    plt.ylabel('MAGNITUDE')
    plt.title(' Plot for FREQUENCY RESPONSE')
    plt.show()

    
    phase=[cmath.phase(H[i])for i in range(len(H))]  # Getting the Phase Response
    
    plt.stem(phase) # Plotting Phase Response
    plt.ylabel('PHASE')
    plt.xlabel('OMEGA')
    plt.title(' Plot For PHASE RESPONSE')
    plt.show()
    
if __name__ == '__main__':
    main()











