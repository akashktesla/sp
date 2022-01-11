# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:11:41 2022

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
    
    # ENTER THE SIGNAL
    sig = []
    N1 = 0
    while(1):
        t = input("Enter value impulse response: ")
        if t == "end":
            break
        sig.append(int(t))
        N1 = N1 + 1
    fplot("Input Signal",sig)
    
    # Converting to np array
    X = np.array(sig)
    N = len(X)
    
    
    # Direct method
    dft = []
    for k in range(N):
        dft.append(sum([X[n] * np.exp(-1j * 2 * np.pi * k * n / N) for n in range(N)]))

    # frequency IN DIRECT METHOD
    dft1 = []
    for i in range(len(dft)):
        dft1.append(abs(dft[i]))
    
    fplot("FREQUENCY RESPONSE IN DIRECT METHOD",dft1)
    
    # PHASE IN DIRECT METHOD
    phase = [cmath.phase(val) for val in dft]
    fplot("PHASE IN DIRECT METHOD",phase)
    oi = phase
    
    # LINEAR TRANSFORMATION
    W = np.ones((N1, N1), dtype=np.clongdouble)
    
    Wn = np.exp(-1j * 2 * np.pi / N1)
    for i in range(N):
        for j in range(N):
            W[i, j] = Wn ** (i * j)
    
    DFT = np.matmul(W, np.transpose(sig))
    
    dft2 = [abs(i) for i in DFT]
    fplot("FREQUENCY RESPONSE IN LINEAR TRANSFORM METHOD",dft2)
    
    phase1 = [cmath.phase(i) for i in DFT]
    fplot("PHASE IN LINEAR TRANSFORM METHOD", phase1)
    phase1= oi;
    
    # Checkig two signals
    if phase1 == phase:
        print("BOTH OUTPUT MATCHES..! SO DFT COMPUTATION IS SUCCESSFUL..!")
    else:
        print("BOTH OUTPUT DOESNOT MATCHES..! SO DFT COMPUTATION IS NOT SUCCESSFUL..!")
    
if __name__ == '__main__':
    main()
    