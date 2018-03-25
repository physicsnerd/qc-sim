import numpy as np

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

done = 'n'

realizations = {}
simulation_type = input("ideal or nonideal simulation: ")

#ADD way to put pi/etc in matrix
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
                save_gate(matrix) #WEIRD it can save a faulty matrix
            return np.dot(matrix, qstat)
        except ValueError:
            print("not same size as vector, not applying")
    else:
        print("Invalid gate (not unitary), not applying")

def save_gate(matrix):
    matrix_name = input('please input a name for your matrix: ')
    file_name = input("please input the file name you would like to create or add too, with file ending if applicable: ")
    with open(file_name, 'a') as myfile:
        myfile.write(matrix_name + ':' + str(matrix) + ' ') #WRITE actual dict?
        
#WRITE probabilities for printing and measurement (n = 1 or 0)
#RESEARCH partial trace see Daniel Sank answer
def probability(qstat, n):
    print("hrm")

#WRITE function that measures
#note: look into how measurement of one qubit affects overall qstat
#qnum: which qubit to measure, default is all are measured, ADD to main running
def measurement(qstat, qnum="all"):
    print("hrm")

#actual running
if simulation_type == 'ideal':
    while done == 'n':
        next_item = input("custom gate or measurement or import: ")
        if next_item == 'measurement':
            qstat = measurement(qstat)
        elif next_item == 'import': #TEST
            file_read = input("input file name you would like to read: ")
            try:
                with open(file_read) as readfile:
                    data = readfile.read()
                    gates = {} #make from data, also figure out how to input data
                    gate_apply = input("which gate from your file would you like to use: ")
                    try:
                        qstat = np.dot(gates[gate_apply],qstat)
                    except ValueError:
                        print("not same size as vector, not applying")
            except FileNotFoundError:
                print("file not found, check your spelling")
        else:
            dimension = int(input("Please give the size of your gate: "))
            qstat = custom_gate(dimension)
            print(qstat)
        done = input("Done with your qubits? y or n: ")

#RESEARCH decoherence times and error correction and noise functions
#WRITE this section of code
#CONSIDER having user import decoherence times they wish, but own noise function
        #nothing special has to be done for error correction
else:
    realization = input("what realization are you using? select from list above: ")

#provides outputs
print("end state: ", qstat)
print("probability of |1> on measurement: ", probability(qstat, 1))
print("probability of |0> on measurement: ", probability(qstat, 0))
