from qutip import *
from matplotlib.pyplot import figure, plot, show
from numpy import linspace, sqrt, array

#Problem size
N = 10
excitations = 3

#parameters
J = 1
Gamma = 0.1

#Times
t0 = 0 
tmax = 25
tnum = 1000

#build operators
dims = [excitations+1]*N
an = enr_destroy(dims, excitations)


#Setup blanks for model
H = Qobj()
decay = []
num_list = []

#Build the Hamiltonian and decay list
for ii in range(N):
    if ii < N-1:
        H += -J*(an[ii+1].dag()*an[ii] + an[ii].dag()*an[ii+1]) 
    decay.append(sqrt(Gamma)*an[ii])
    num_list.append(an[ii].dag()*an[ii])

#Set up initial conditions
initial_dims = [excitations]
initial_dims.extend([0]*(N-1))
initial = enr_fock(dims, excitations, initial_dims)
tlist = linspace(t0, tmax, tnum)

#Solve it
result = mesolve(H, initial, tlist, decay, num_list)
expect_array = array(result.expect)

#Plot it
figure()
plot(tlist, expect_array.T)
show(block=False)
