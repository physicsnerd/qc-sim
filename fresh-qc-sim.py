import numpy as np
import random
import math
import itertools
#save on github!!!!!!!!
#check over var name use - clean up and see what is being reassigned

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
for i in range (0, 2**qnum):
    basis_states.append(bin(i)[2:].zfill(qnum))
done = 'n'

realizations = {}
gates = {}
simulation_type = input("ideal or nonideal simulation: ")

#ADD way to put pi/sqrt/i/etc in matrix
def custom_gate(dimension):
    ls = []
    for y in range(dimension): 
        for x in range(dimension):
            ls.append(float(input('What value for position ({}, {}): '.format(y+1, x+1))))
    matrix = np.matrix(np.resize(ls, (dimension, dimension)))
    if np.array_equal(np.dot(matrix, matrix.conj().T), np.identity(dimension)) == True:
        try:
            save = input("Would you like to save this gate? y or n: ")
            if save == 'y':
                print('note that this can save a non-unitary matrix')
                save_gate(matrix)
            return np.dot(matrix, qstat)
        except ValueError:
            print("not same size as vector, not applying")
    else:
        print("Invalid gate (not unitary), not applying")

#look into np.loadtxt and np.savetxt and get the name for matrix from file name?
def save_gate(matrix):
    matrix_name = input('please input a name for your matrix: ')
    #file_name = input("please input the file name you would like to create or add too, with file ending if applicable: ")
    gates[matrix_name] = matrix
    np.savetxt(matrix_name+'.txt', matrix, delimiter=',')

def apply(matrix, qstat):
    try:
        return np.dot(matrix, qstat)
    except ValueError:
        print("not same size as vector, not applying")

def norm(qstat):
    return math.sqrt(sum([x**2 for x in list(qstat)]))

def normalize(qstat):
    norm = norm(qstat)
    return 1/math.sqrt(norm)*qstat#scalar multiplication numpy? check right

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
        print('hmm')
    else:
        #do overall
        print('hmm')

#go through which qnum is intended and where
#figure out how probability arguments should be handled
def measurement(qstat, qnum="all"):
    if qnum != "all":
        qnum = int(qnum)
        #fill in
        zero_prob = probability(qstat, 0, qnum)
        rand = random.random()
        acceptable_stats = []
        if rand < zero_prob:
            #zero
            for i in basis_states:
                if i[qnum] == '0':
                    acceptable_stats.append(i)
            
        else:
            #one
            for i in basis_states:
                if i[qnum] == '1':
                    acceptable_stats.append(i)
        projection = projection(acceptable_stats)
        return normalize(np.dot(projection, qstat))
    else:
        zero_prob = probability(qstat, 0, qnum)
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
            try:#TEST!!!
                matrix_load = np.loadtxt(file_read, dtype='i', delimiter=',')#change dtype for floats?
                gates[file_read[:file_read.index('.')]] = matrix_load
                print(gates)
                matrix = input("which gate from your file would you like to use: ")
                qstat = apply(gates[matrix], qstat)
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
    #probably different probability issue than with measurement...?
print("end state: ", qstat)
#rewrite based on basis-states list
print("probability of |1> on measurement: ", probability(qstat, 1))
print("probability of |0> on measurement: ", probability(qstat, 0))
