import numpy as np
import random

qnum = int(input("How many qubits: "))

zero_state = np.matrix([[1],[0]])
one_state = np.matrix([[0],[1]])
z_or_o = input('would you like to start in the 0 or 1 state: ')
iterate = 1
while iterate <= qnum:
    if iterate == 1:
        if z_or_o == '0':
            x = zero_state
        elif z_or_o == '1':
            x = one_state
    if iterate == qnum:#change to elif?
        qstat = x
        print(qstat)
    else:
        x = np.kron(x,zero_state)
    iterate+=1
