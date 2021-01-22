import numpy as np
import math
import cmath
from functools import reduce

qnum = int(input('number of qubits: '))

def gate_scale(gate, ap_qubit):
    matrix_list = []
    dimensions = int(math.sqrt(np.size(gate)))
    identity_matrix = np.identity(dimensions, np.matrix)

    #generate list
    if ap_qubit == 'all':
        for i in range(qnum):
            matrix_list.append(gate)
    else:
        ap_qubit = int(ap_qubit)
        for i in range(qnum):
            matrix_list.append(identity_matrix)
        matrix_list[ap_qubit-1] = gate
    
    #iterate through list
    return reduce(np.kron, matrix_list)

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
ap_qubit = input('qubit to apply to: ')
matrix = gate_scale(matrix, ap_qubit)
print(matrix)
save_gate(matrix)
