from qutip import sigmax, fock, sigmaz, mesolve, qeye, tensor, destroy
from matplotlib.pyplot import figure, plot, show
from numpy import linspace, sqrt

#Problem size
Nphot = 10

#Parameters
Om0 = 1.0
OmC = 1.0
kappa = 0.1
g = 0.3

#Basis operators
Is = qeye(2)
Iphot = qeye(Nphot)
a = destroy(Nphot)

#Define the model
H = 0.5*Om0*tensor(sigmaz(), Iphot) + OmC*tensor(Is, a.dag()*a) + g*tensor(sigmax(), a + a.dag())
decay = [sqrt(kappa)*tensor(Is, a)] 

#initial state and expectation values
init = tensor(fock(2,0), fock(Nphot,0))
tlist = linspace(0,50,500)
op = [tensor(sigmaz(), Iphot), tensor(Is, a.dag()*a)]

#Solve it
result = mesolve(H, init, tlist, decay, op)

#plot it
figure(1)
plot(tlist, result.expect[0])
plot(tlist, result.expect[1])
show(block=False)


