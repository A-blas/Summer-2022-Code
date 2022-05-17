import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x1 = np.linspace(0, 7, 90)
y1 = 0 * x1 +0.24

x2 = np.linspace(0, 7, 90)
y2 = np.sin(2 *x2) 
y2 +=  0.5 + 0.18 * np.sin(11 * x2) 
y2 += -0.9 + 0.0045 * np.sin(115 * x2) 
y2 += 0.25 + 0.00017 * np.sin(1000 * x2) 
y2 += 1 + 0 * np.cos(x2)

# plot
fig, ax = plt.subplots()

ax.plot(x1, y1, linewidth=1.0)
ax.plot (x2, y2, linewidth=1.0)

ax.set(xlim=(1, 5), xticks=np.arange(0, 4),
       ylim=(-3, 5), yticks=np.arange(-1, 4))

plt.show()