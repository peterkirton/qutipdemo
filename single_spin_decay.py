from qutip import sigmax, fock, sigmaz, mesolve, sigmam
from pylab import figure, plot, show
from numpy import linspace, sqrt


Om = 0.5
gam = 0.1

H = Om*sigmax()
decay = sqrt(gam)*sigmam()

init = fock(2,1)
tlist = linspace(0,50,500)
op = sigmaz()

result = mesolve(H, init, tlist, decay, op)

figure()
plot(tlist, result.expect[0])

show(block=False)


