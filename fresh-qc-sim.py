import numpy as np
import random
import math

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

basis_states = [] #is this generation even correct? check with mr. maine...?
for i in range(0, 2**qnum):
    basis_states.append(bin(i)[2:].zfill(qnum))
done = 'n'

realizations = {}#not yet in use
gates = {}
simulation_type = input("ideal or nonideal simulation: ")

#ADD way to put pi/sqrt/i/etc in matrix
def custom_gate(dimension):
    value_hold = []
    for y in range(dimension):
        for x in range(dimension):
            value_hold.append(float(input('What value for position ({}, {}): '.format(y+1, x+1))))
    matrix = np.matrix(np.resize(value_hold, (dimension, dimension)))
    if np.array_equal(np.dot(matrix, matrix.conj().T), np.identity(dimension)) == True:
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
    return math.sqrt(sum([x**2 for x in list(qstat)]))

def normalize(qstat):
    norm = norm(qstat)
    return 1/math.sqrt(norm)*qstat#scalar multiplication numpy? check if right

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
      
#WRITE probabilities for printing and measurement (n = 1 or 0)
#RESEARCH partial trace see Daniel Sank forum answer ask Harry?
#FIGURE OUT what does this even need to look like? where am i calling from? &c
def probability(qstat, pn, qn = "all"):
    if qn == "all":
        #do normal
        return None#placeholders
    else:
        #do overall
        return None

#figure out how probability arguments should be handled
def measurement(qstat, qnum_meas="all"):
    if qnum_meas != "all":
        qnum_meas = int(qnum_meas)
        zero_prob = probability(qstat, 0, qnum_meas)
        rand = random.random()
        acceptable_stats = []
        if rand < zero_prob:
            #zero
            for i in basis_states:
                if i[qnum_meas] == '0':
                    acceptable_stats.append(i)
            
        else:
            #one
            for i in basis_states:
                if i[qnum_meas] == '1':
                    acceptable_stats.append(i)
        projection = projection(acceptable_stats)
        return normalize(np.dot(projection, qstat))
    else:
        zero_prob = probability(qstat, 0, qnum_meas)
        random_num = random.random()
        if random_num < zero_prob:
            return zero_stat
        else:
            return one_stat

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
                matrix_load = np.loadtxt(file_read, dtype='i', delimiter=',')#change dtype for floats?
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

#RESEARCH decoherence times and error correction and noise functions
#WRITE this section of code
#CONSIDER having user import decoherence times they wish, but own noise function
        #nothing special has to be done for error correction?
else:
    print('this is not written yet; sorry!')
    #realization = input("what realization are you using? select from list above: ")

#provides output
print("end state: ", qstat)

for i in basis_states:
    print('probability of |'+i+'> on measurement: ', probability(qstat, i))
