# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 14:17:03 2022

@author: cb.en.u4cce19027
"""
# Importing Libraries
import numpy as np 
import matplotlib.pyplot as plt 


x1 = [2,4,7,3]  # Given Signal 1
x2 = [1,2,5,3]  # Given Signal 1

# CHECKING LINEARITY

# ADDITIVITY
X1 = []
for i in range(len(x1)):
    X1.append(x1[i]+x2[i])
    
# HOMOGINITY y[n] = nx[n]
Y1 = []
for i in range(len(X1)):
    Y1.append(i*X1[i])
    
s = np.arange(0,len(Y1),1)


plt.title("SIGNAL 1")
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.stem(s,x1)
plt.show()

plt.title("SIGNAL 2")
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.stem(s,x2)
plt.show()

plt.title("ADDITIVITY THEN HOMOGINITY")
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.stem(s,Y1)
plt.show()

# HOMOGINITY THEN ADDITIVITY

y1 = []
y2 = []

# HOMOGINITY y[n] = nx[n]
for i in range(len(x1)):
    y1.append(i*x1[i])
    
for i in range(len(x2)):
    y2.append(i*x2[i])

# ADDITIVITY
Y2 = []
for i in range(len(y1)):
    Y2.append(y1[i]+y2[i])
    
s = np.arange(0, len(Y2), 1)  # Number of Samples

plt.title("HOMOGINITY THEN ADDITIVITY")
plt.stem(s, Y2)
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.show()

if Y1 == Y2:
    print("\n System is LINEAR\n")
else:
    print("\n System is NOT LINEAR\n")
    
# TIME INVARIANT

s = np.arange(0, len(x1), 1) # Number of Samples
plt.title("SIGNAL 1 BEFORE PASSING INTO SYSTEM")
plt.stem(s, x1)
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.show()


# INPUT -> SYSTEM -> DELAY -> OUTPUT

# PASSING INTO SYSTEM
y1 = []
for i in range(len(x1)):
    y1.append(x1[i]*i)
    
s = np.arange(0, len(y1),1)
plt.title("MODULE 1: SIGNAL 1 AFTER PASSING INTO SYSTEM")
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.stem(s, y1)
plt.show()

# DELAY OF (t-T)
yt1 = []
shiftr = 3

for i in range(shiftr):
    yt1.append(0)
    
for i in range(len(y1)):
    yt1.append(y1[i])
    
s = np.arange(0, len(yt1), 1)
plt.stem(s, yt1)
plt.title("MODULE 1: SIGNAL 1 AFTER DELAY OF (t-3)")
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.show()



# INPUT -> DELAY -> SYSTEM -> OUTPUT

# DELAY OF (t-T)
xt1 = []
shiftr = 3
for i in range(shiftr):
    xt1.append(0)
    
for i in range (len(x1)):
    xt1.append(x1[i])
    
s = np.arange(0, len(xt1), 1)
plt.stem(s, xt1)
plt.title("Delay of t-T")
plt.title("MODULE 2: SIGNAL 1 AFTER DELAY OF (t-3)")
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.show()

# PASSING INTO SYSTEM
xs1 = []
for i in range(len(xt1)):
    xs1.append(xt1[i]*i)
    
s = np.arange(0, len(xs1), 1)
plt.stem(s, xs1)
plt.title("MODULE 2: SIGNAL 1 AFTER PASSING INTO SYSTEM")
plt.xlabel('SAMPLES')
plt.ylabel('AMPLITUDE')
plt.show()

if yt1 == xs1:
    print("\n System is TIME INVARIANT\n")
else:
    print("\n System is NOT TIME INVARIANT\n")
    