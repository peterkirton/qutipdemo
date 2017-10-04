from qutip import sigmax, fock, sigmaz, mesolve
from matplotlib.pyplot import figure, plot, show
from numpy import linspace


Om = 0.5
H = Om*sigmax()
init = fock(2,1)
tlist = linspace(0,50,500)
op = sigmaz()

result = mesolve(H, init, tlist, [], op)

figure()
plot(tlist, result.expect[0])

show(block=False)


