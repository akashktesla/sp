# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:42:02 2022

@author: cb.en.u4cce19027
"""
import numpy as np
import matplotlib.pyplot as plt

# SINE WAVE
time = np.linspace(-0.2,0.05,1000)
amplitude = 325
frequency = 100
signal1 = amplitude*np.sin(np.pi*frequency*time)

# PLOTTING SINE WAVE
plt.plot(time,signal1)
plt.xlabel('TIME PERIOD')
plt.ylabel('AMPLITUDE')
plt.title('TIME DOMAIN PLOT FOR SINUSODIAL PLOT..!')
plt.show()

# UNIT IMPULSE
samples = range(0, 10, 1)
signal2 = []
for i in range(len(samples)):
    temp = (1 if samples[i]==0 else 0)
    signal2.append(temp)

# PLOTTING UNIT IMPULSE PLOT
plt.stem(samples, signal2)
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.title('UNIT IMPULSE PLOT')
plt.show()

# UNIT STEP FUNCTION
sample = range(0, 10, 1)
signal3 = []
for i in range(len(sample)):
    temp = (1 if sample[i]>=0 else 0)
    signal3.append(temp)
    
# PLOTTING UNIT IMPULSE PLOT
plt.stem(sample, signal3)
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.title('UNIT STEP FUNCTION PLOT')
plt.show()


