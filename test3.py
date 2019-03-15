import numpy as np
import math
qnum = 1
savedgates = {}

fileholdings = 'not:0110 id:1001 bigid:100010001'

split1 = fileholdings.split(' ')
split2 = []
for i in split1:
   split2.append(i.split(':'))
for i in split2:
   savedgates[i[0]] = i[1]

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

for i in savedgates:
   savedgates[i] = np.matrix(savedgates[i])
