import math
import numpy as np
import matplotlib.pyplot as plt
def my_formula(x):
    a=int(input("what is coefficient of x^2: "))
    b=int(input("What is coefficient of x:   "))
    c=int(input("What is value of constant c:")) 
    return a*(x**2)+b*(x)+c
    d=(b*b-4*a*c)
    print("dis",d)
def graph(formula,range):
    x=np.array(range)
    y=formula(x)
    plt.plot(x,y)
    plt.show()
graph(my_formula,range(-10,11))