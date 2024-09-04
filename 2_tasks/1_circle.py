from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pist_xy = np.array([np.radians(deg) for deg in [30, 45, 60, 90, 120, 135, 150, 180, 270]])
nim=np.array([1,2,4,6, 8, 10, 12, 14, 16])

print(pist_xy)
print(nim)
colors=np.array(['red', 'green', 'blue', 'orange','red', 'green', 'blue', 'orange','orange'])

text=[r'$\pi$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\frac{\pi}{6}$', '', '' '', '', '', '']

x = np.cos(pist_xy/nim)
y = np.sin(pist_xy/nim)

plt.scatter(x, y, color=colors, marker='X')
print(len(text))

for i in range(len(pist_xy)):
    plt.annotate(text[i],
             xy=(np.cos(pist_xy[i]/nim[i]), np.sin(pist_xy[i]/nim[i])), xycoords='data',
             xytext=(+30, +5), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))


plt.show()