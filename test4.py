import numpy as np
gates = {}
#read
file_name = input("file name w/ extension: ")
matrix_load = np.loadtxt(file_name, dtype='i', delimiter=',')
gates[file_name[:file_name.index('.')]] = matrix_load
print(gates)
#write
a = np.matrix([[0,1],[1,0]])
gate_name = input("name of gate: ")
np.savetxt(gate_name+'.txt', a, delimiter=',')
