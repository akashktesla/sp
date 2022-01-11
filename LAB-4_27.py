import numpy as np
import matplotlib.pyplot as plt

# Function to perform Convolution
def convolve(x, h):
    y = []
    for i in range(len(x)):
        h1 = np.append([0] * i, h) # Shifting 
        h1 = np.append(h1,  [0] * (len(x) - 1 - i))  # Shifting
        h1 *= x[i] # Multiplying the shifted signal
        y.append(h1)      
    return y, np.sum(y, axis=0).tolist()  # Adding


# Function to Plot
def fplot(t,x):
    plt.stem(x)
    plt.title(t)
    plt.xlabel('SAMPLES')
    plt.ylabel('AMPLITUDE')
    plt.show()

def main():
    
    # Input Signal
    IS = []
    n = 0
    while(1):
        t = input("Enter value input signal : ")
        if t == "end":
            break
        IS.append(int(t))
        n = n + 1
    

    
    # Impulse response
    IR = []
    I = 0
    while(1):
        t = input("Enter value impulse response: ")
        if t == "end":
            break
        IR.append(int(t))
        I = I + 1
    
    # Input Signal Plot    
    fplot('INPUT SIGNAL', IS)
    
    # Impulse response Plot
    fplot('IMPULSE RESPONSE', IR)
    
    yi, y = convolve(IS, IR) # Calling Convolution Function
    
    # Converting Float values to INT
    for i in range(len(y)):
        y[i] = int(y[i])
        
        
    # Plotting the Graph
    fplot('SYSTEM RESPONSE PLOT AFTER CONVOLUTING', y)


if __name__ == '__main__':
    main()










