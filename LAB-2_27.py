# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:04:21 2022

@author: cb.en.u4cce19027
"""

import numpy as np
import matplotlib.pyplot as plt

# UNIT STEP FUNCTION
sample = range(0, 10, 1)
signal1 = []
for i in range(len(sample)):
    temp = (1 if sample[i]>=0 else 0)
    signal1.append(temp)

    
# PLOTTING UNIT IMPULSE PLOT
plt.stem(sample, signal1)
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.title('UNIT STEP FUNCTION 1')
plt.show()

n = np.arange(0,10,1)
        
u2 = []
for i in range(len(n)):
    if n[i]>=2:
        u2.append(1)
    else:
        u2.append(0)

    
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.title('Question 1')
plt.stem(n,u2)
plt.xticks(np.arange(10))
plt.yticks(np.arange(0,3,1))
plt.show()


sample1 = range(0, 5, 1)
signal2 = [2, 3, 4, 5, 0]
plt.stem(sample1, signal2)
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.title('Question 2')
plt.show()


samples3 = range(-6,7,1)
x = [0,0,0,3,2,1,0,1,2,3,0,0,0]
plt.stem(samples3, x)
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.title('Question 3 Signal 1')
plt.show()

y = [0,0,-1,-1,-1,-1,0,1,1,1,1,0,0]
plt.stem(samples3, y)
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.title('Question 3 Signal 2')
plt.show()
x1 = x
y1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1, 4,1):
    x1[i] = x[3*i-1]

for i in range(2,11,1):
    y1[i] = x[i-2] + y[i+2]
    
plt.stem(samples3, x1)
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.title('Question 3.1')
plt.show()

plt.stem(samples3, y1)
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.title('Question 3.2')
plt.show()



