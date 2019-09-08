import numpy as np
import math
import cmath

qnum = int(input('number of qubits: '))

def gate_scale(gate, ap_qubit):
    dimensions = int(math.sqrt(np.size(gate)))
    ap_qubit-=1
    if 2**qnum == dimensions:
        return gate
    else:
        iterator = 1
        kron_num = []
        identity = np.identity(dimensions, np.matrix)
        while iterator <= dimensions:
            kron_num.append(identity)
            iterator+=1
        kron_num[ap_qubit] = gate
        kron_iterator = list(range(len(kron_num)))
        for i in kron_iterator:
            if i == 0:
                x = kron_num[i]
            if i > 0:
                x = np.kron(x, kron_num[i])
        return x

def save_gate(matrix):
    matrix_name = input('please input a name for your matrix: ')
    np.savetxt(matrix_name+'.txt', matrix, delimiter=',')
    

dimension = int(input('size of matrix: '))
value_hold = []
for y in range(dimension):
    for x in range(dimension):
        value_hold.append(eval(input('What value for position ({}, {}): '.format(y+1, x+1))))
matrix = np.matrix(np.resize(value_hold, (dimension, dimension)))
ap_qubit = int(input('qubit to apply to: '))
print(gate_scale(matrix, ap_qubit))
save_gate(matrix)
