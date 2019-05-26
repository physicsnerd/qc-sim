import numpy as np
import random
import math
import cmath#so eval can work w/ complex #s

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
    if iterate == qnum:
        qstat = x
        print(qstat)
    else:
        x = np.kron(x,zero_state)
    iterate+=1

basis_states = []
for i in range(0, 2**qnum):
    basis_states.append(bin(i)[2:].zfill(qnum))
done = 'n'

gates = {}
simulation_type = input("ideal or nonideal simulation: ")

#for 'j' write '1j'
#eventually change eval() to custom parser...
def custom_gate(dimension):
    value_hold = []
    for y in range(dimension):
        for x in range(dimension):
            value_hold.append(eval(input('What value for position ({}, {}): '.format(y+1, x+1))))
    matrix = np.matrix(np.resize(value_hold, (dimension, dimension)))
    if np.allclose(np.dot(matrix, matrix.conj().T), np.eye(dimension)):
        try:
            save = input("Would you like to save this gate? y or n: ")
            if save == 'y':
                save_gate(matrix)
            return np.dot(matrix, qstat)
        except ValueError:
            print("not same size as vector, not applying")
            return qstat
    else:
        print("Invalid gate (not unitary), not applying")
        return qstat

def save_gate(matrix):
    matrix_name = input('please input a name for your matrix: ')
    gates[matrix_name] = matrix
    np.savetxt(matrix_name+'.txt', matrix, delimiter=',')

def apply(matrix, qstat):
    try:
        return np.dot(matrix, qstat)
    except ValueError:
        print("not same size as vector, not applying")
        return qstat

def norm(qstat):
    return math.sqrt(np.sum(np.square(qstat)))

def normalize(qstat):
    norm_result = norm(qstat)
    return np.dot(1/math.sqrt(norm_result),qstat)

def projection(acceptable_stats):
    #create qnum*qnum diagonal matrix
    diag_gen = []
    for i in range(0, qnum**2):
        diag_gen.append(1)
    diagonal_matrix = np.diag(diag_gen)
    #list of indexes of allowed states
    position_nums = []
    for i in acceptable_stats:
        position_nums.append(basis_states.index(i))
    #modify diagonal matrix to comply with list
    for i in range(0, qnum**2):
        if i not in position_nums:
            for k in range(0, qnum**2):
                diagonal_matrix[i][k] = 0
    return diagonal_matrix

def probability(qstat, qnum_index):
    amplitude = np.array(qstat)[qnum_index][0]
    prob = abs(amplitude)**2
    return prob

#review != 'all' section
def measurement(qstat, qnum_meas="all"):
    if qnum_meas != "all":
        qnum_meas = int(qnum_meas)
        zero_prob = 1 - probability(qstat, qnum_meas-1)
        rand = random.random()
        acceptable_stats = []
        if rand < zero_prob:
            #zero
            for i in basis_states:
                if i[qnum_meas-1] == '0':
                    acceptable_stats.append(i)
        else:
            #one
            for i in basis_states:
                if i[qnum_meas-1] == '1':
                    acceptable_stats.append(i)
        projection_result = projection(acceptable_stats)
        return normalize(np.dot(projection_result, qstat))
    else:
        probabilities = []
        for i in qstat:
            probabilities.append(probability(qstat, np.where(qstat==i)[0][0]))
        rand_int = random.random()
        zero_vector = np.zeros((qnum**2, 1))
        counter = 0
        for i in probabilities:
            if rand_int < sum(probabilities[:counter+1]):
                zero_vector[counter][0] = 1
                return zero_vector
            counter+=1

#actual running
if simulation_type == 'ideal':
    while done == 'n':
        next_item = input("custom gate or measurement or import or prev used: ")
        if next_item == 'measurement':
            measure_num = input('input all or which qubit num you would like measured: ')
            qstat = measurement(qstat, measure_num)
            print(qstat)
        elif next_item == 'import':
            file_read = input("input file name you would like to read: ")
            try:
                matrix_load = np.loadtxt(file_read, delimiter=',')
                gates[file_read[:file_read.index('.')]] = matrix_load
                print(gates)
                try:
                    matrix = input("which gate from your file would you like to use: ")
                    qstat = apply(gates[matrix], qstat)
                except KeyError:
                    print('this gate does not seem to have been saved in the past. try custom gate')
                print(qstat)
            except FileNotFoundError:
                print("file not found, check your spelling")
        elif next_item == 'prev used':
            print('list of gates: ',gates)
            matrix = input("please input the matrix name: ")
            try:
                qstat = apply(gates[matrix],qstat)
                print(qstat)
            except KeyError:
                print("this gate does not seem to have been saved in the past. try custom gate")
        else:
            dimension = int(input("Please give the size of your gate: "))
            qstat = custom_gate(dimension)
            print(qstat)
        done = input("Done with your qubits? y or n: ")

#consider having user import decoherence times they wish, but own noise function
#nothing special has to be done for error correction?
else:
    print('this is not written yet; sorry!')

#provides output
print("end state: ", qstat)

for i in basis_states:
    print('probability of |'+i+'> on measurement: ', probability(qstat, basis_states.index(i)))
