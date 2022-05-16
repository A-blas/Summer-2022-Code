import matplotlib.pyplot as plt #makes visual stuff and animations
import numpy as np #good for computing numbers

plt.style.use('_mpl-gallery') #the "style" helpsdetermine what type of visual is needed

# make data
x = np.linspace(0, 5, 10) #idk but this definitely controlled how smooth the curves were
y = 5 + 2 * np.sin(3 * x) #amplitude

# plot
fig, ax = plt.subplots() #tuple? makes the axes?

ax.plot(x, y, linewidth=3.0) #thickness of line on graph

ax.set(xlim=(-3, 10), xticks=np.arange(-2, 10), #these both set parameters in the x and y axis
       ylim=(-3, 10), yticks=np.arange(-2, 10))

plt.show() #actually open image in a new tab