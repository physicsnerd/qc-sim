import numpy as np
import math
import cmath

qnum = int(input('number of qubits: '))

def gate_scale(gate, ap_qubit):#this does not work
    dimensions = int(math.sqrt(np.size(gate)))
    ap_qubit-=1
    if 2**qnum == dimensions:
        return gate
    else:
        iterator = 1
        kron_num = []
        identity = np.identity(dimensions, np.matrix)
        while iterator <= qnum:#changed from <= dimensions to <= qnum
            kron_num.append(identity)
            iterator+=1
        kron_num[ap_qubit] = gate
        kron_iterator = list(range(len(kron_num)))
        #has to be a better way to do this chunk of code
        for i in kron_iterator:
            if i == 0:
                x = kron_num[i]
            if i > 0:
                x = np.kron(x, kron_num[i])
        return x

def save_gate(matrix):
    matrix_name = input('please input a name for your matrix: ')
    np.savetxt(matrix_name+'.txt', matrix, delimiter=',')
    

dimension = int(input('size of matrix to scale: '))
value_hold = []
for y in range(dimension):
    for x in range(dimension):
        element = input('What value for position ({}, {}): '.format(y+1, x+1))
        element.strip("\"\'\\\/") #to sanitize input
        value_hold.append(eval(element))
matrix = np.matrix(np.resize(value_hold, (dimension, dimension)))
ap_qubit = int(input('qubit to apply to: '))
matrix = gate_scale(matrix, ap_qubit)
print(matrix)
save_gate(matrix)
