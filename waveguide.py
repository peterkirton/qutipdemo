from qutip import *
from matplotlib.pyplot import figure, plot, show
from numpy import linspace, sqrt, array

#Problem size
N = 10
excitations = 3

tlist = linspace(0, 25,1000)

#parameters
J = 1
Gamma = 0.1

#build operators
dims = [excitations]*N

initial_dims = [excitations-1]
initial_dims.extend([0]*(N-1))

an = enr_destroy(dims, excitations)
initial = enr_fock(dims, excitations, initial_dims)

#Setup blanks for model
H = Qobj()
decay = []
num_list = []

for ii in range(N):
    if ii < N-1:
        H += -J*(an[ii+1].dag()*an[ii] + an[ii].dag()*an[ii+1]) 
    decay.append(sqrt(Gamma)*an[ii])
    num_list.append(an[ii].dag()*an[ii])

result = mesolve(H, initial, tlist, decay, num_list)

expect_array = array(result.expect)

figure()
plot(tlist, expect_array.T)
show(block=False)
