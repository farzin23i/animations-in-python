import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

h= 1e-2
x= int (1/h)-1
y= int (1/h)-1
v= np.zeros ([y+1,x+1])

for i in range (1, x):
  for j in range (1, y):
    v[j, i]= np.random.rand ()

v[:,x]= 1

fig = plt.figure()
im= plt.imshow (v, animated=True, interpolation= 'gaussian')

"""
===================
  RELAX THE POTENTIAL
===================
"""
def relax (v):
    for i in range (1,x):
        for j in range (1,y):
            #if (y-j!=50 or i<=45 or i>=55):
                #v[j,i]= 0.25 * (v[j-1,i] + v[j,i+1] + v[j+1,i] + v[j,i-1])
    
            v[y-j,i]= 0.25 * (v[y-j-1,i] + v[y-j,i+1] + v[y-j+1,i] + v[y-j,i-1])
    return v
"""
===================
  ANIMATE THE CHANGES
===================
"""
def updatefig(*args):
    im.set_array(relax(v))
    return im,
ani = animation.FuncAnimation(fig, updatefig, interval=1, blit=True)
plt.show()
