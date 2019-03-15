import numpy as np
qnum = 2
basis_states = ['00', '01', '10', '11']
def projection(acceptable_stats):
    #create qnum*qnum diagonal matrix
    diag_gen = []
    for i in range(0, qnum**2):
        diag_gen.append(1)
    diagonal_matrix = np.diag(diag_gen)
    position_nums = []
    for i in acceptable_stats:
        position_nums.append(basis_states.index(i))
    for i in range(0, qnum**2):
        if i not in position_nums:
            for k in range(0, qnum**2):
                diagonal_matrix[i][k] = 0
    return diagonal_matrix

print(projection(['01', '11']))
print(projection(['00', '01']))
