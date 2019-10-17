import numpy as np
from scipy.integrate import ode
from scipy.special import jv
from matplotlib.pyplot import figure, plot, show

#Defien the ODE function
def func(x,vy):
    v,y = vy
    return [-5*y + jv(0,x), v]
    

#Parameters
xmax = 15
dx = 0.1

ylist = []
xlist = []

#Build the model
r = ode(func)
r.set_initial_value([0,0], 0)

#Propogate
while r.successful() and r.t < xmax:
    xlist.append(r.t)
    output = r.integrate(r.t+dx)
    ylist.append(output[1])
    
#Plot
figure()
plot(xlist, ylist)
show(block=False)
    
