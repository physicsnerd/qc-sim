#with open(file_read) as readfile:#see notes on save file function
                    
                    '''
                    fileholdings = readfile.read()
                    savedgates = {}
                    #move from string into dictionary
                    split1 = fileholdings.split(' ')
                    split2 = []
                    for i in split1:
                        split2.append(i.split(':'))
                    print(split2)
                    for i in split2:
                        savedgates[i[0]] = i[1]#still not quite working
                    #generate nested list of integers from strings
                    for i in savedgates:
                        string_matrix = savedgates[i]
                        rows = []
                        row = []
                        index = 1
                        for k in string_matrix:
                            row.append(int(k))
                            m_size = int(math.sqrt(len(string_matrix)))
                            if index%m_size == 0:
                                rows.append(row)
                                row = []
                            index+=1
                        savedgates[i] = rows
                    #convert nested lists to matrices
                    for i in savedgates:
                        savedgates[i] = np.matrix(savedgates[i])
                    #add savedgates to gates
                    for i in savedgates:
                        gates[i] = savedgates[i]
                    #apply gate
                    '''
