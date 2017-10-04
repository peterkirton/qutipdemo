from qutip import sigmax, fock, sigmaz, mesolve, qeye, tensor, destroy
from matplotlib.pyplot import figure, plot, show
from numpy import linspace, sqrt

Nphot = 10

Om0 = 1.0
OmC = 1.0

kappa = 0.1

g = 0.3

Is = qeye(2)
Iphot = qeye(Nphot)
a = destroy(Nphot)

H = Om0/2.0 * tensor(sigmaz(), Iphot) + OmC*tensor(Is, a.dag()*a) + g*tensor(sigmax(), a + a.dag())
decay = [sqrt(kappa)*tensor(Is, a)] 

init = tensor(fock(2,0), fock(Nphot,0))
tlist = linspace(0,50,500)
op = [tensor(sigmaz(), Iphot), tensor(Is, a.dag()*a)]

result = mesolve(H, init, tlist, decay, op)

figure(1)
plot(tlist, result.expect[0])
plot(tlist, result.expect[1])

show(block=False)


