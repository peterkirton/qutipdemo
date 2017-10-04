from qutip import sigmax, fock, sigmaz, mesolve, sigmam, sigmap, qeye, tensor
from matplotlib.pyplot import figure, plot, show
from numpy import linspace, sqrt


Om1 = 2.0
Om2 = 1.0

gam1 = 0.1
gam2  = 0.2

g = 0.3

Is = qeye(2)

H = Om1*tensor(sigmax(), Is) + Om2*tensor(Is, sigmax()) + g*(tensor(sigmam(), sigmap()) + tensor(sigmap(), sigmam()))
decay = [sqrt(gam1)*tensor(sigmam(), Is), sqrt(gam2)*tensor(Is, sigmam())] 

init = tensor(fock(2,1), fock(2,0))
tlist = linspace(0,50,500)
op = [tensor(sigmaz(), Is), tensor(Is, sigmaz())]

result = mesolve(H, init, tlist, decay, op)

figure()
plot(tlist, result.expect[0])
plot(tlist, result.expect[1])

show(block=False)


