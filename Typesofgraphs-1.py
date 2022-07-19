import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-2, 20*np.pi, 0.3)

f = lambda x,a : a * x**2

a= 10 

y =  f(x,a)
y2 = np.log10(y)
y3 = -3*x**2 - 2*x - 4
y4 = 12*x - 7
y5 = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y)
ax.plot(x, y3)
ax.plot(x, y4)
ax.plot(x, y5)

plt.title('Types of functions')
plt.xlabel("X")
plt.ylabel("Y")

eq1= r'$\log_{10}$'
eq2= '$-3x^{2}$' 
eq3= '12x - 7'
eq4= 'cos(x)'

tot = 'Blue: y='+ eq1, 'Orange: y='+ eq2, 'Green: y='+ eq3, 'Red: y='+ eq4

plt.legend(tot)

plt.show()

