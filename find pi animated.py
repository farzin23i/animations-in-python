'''
This is a code for finding "pi" number using monte carlo method. 
In this code there is a scatter animated plot. Also you can find out useful tips on how to update texts in animations.
'''

import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L= 1
x= []
y= []
xcir= []
ycir= []
c= 0
def rnd (N):
    global x, y, xcir, ycir, c
    for i in range (N):
        x1= (random.uniform (-L, L))
        y1= (random.uniform (-L, L))
        r= np.sqrt (x1**2 + y1**2)
        x.append(x1)
        y.append(y1)
        if r<= 1:
            xcir.append(x1)
            ycir.append(y1)
            c+= 1
N= 10
rnd(N)
fig = plt.figure()
im= plt.plot (x, y, "c.", xcir, ycir, "r.", animated= True)
plt.axis ([-1.1,1.1, -1.1,1.3])
a= plt.suptitle ("Finding The PI", fontweight='bold')
txt1= 'Finding The PI with %.0f Dots'
txt2= 'Pi= %.6f '
txt3= 'ERROR= %.6f '
t1 = plt.text(-.95, 1.15, '',color ='k')
t2 = plt.text(-.95, 1.03, '',color ='k', fontweight='bold')
t3 = plt.text(0, 1.03, '',color ='m')
def updatefig(t, *args):
    global N
    nn= int(t**2/1000)
    N+= nn
    rnd(nn)
    im[0].set_xdata(x)
    im[0].set_ydata(y)
    im[1].set_xdata(xcir)
    im[1].set_ydata(ycir)
    Pi= c*4/N
    t1.set_text(txt1 % N)
    t2.set_text(txt2 % Pi)
    t3.set_text(txt3 % abs(np.pi - Pi))
    return t1, t2, t3, im[0], im[1]
ani = animation.FuncAnimation(fig, updatefig, interval=10, blit=True)
plt.show()
