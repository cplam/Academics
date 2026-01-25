import numpy as np

a_s = np.array([2,3,5,6,5,7])
row = len(a_s)
col = row//2 + row%2

Rough_table = np.zeros((row, col))
if row%2 != 0: # Even degree
    a_s = np.append(a_s,0)
a_s = a_s.reshape(-1,2).transpose()
Rough_table[0:2,:] = a_s



for i in range(2,row):
    for j in range(col-1):
        Rough_table[i][j] = Rough_table[i-2][0] * Rough_table[i-1][j+1] - Rough_table[i-2][j+1] * Rough_table[i-1][0]
        if Rough_table[i-1][0] != 0:
            Rough_table[i][j] /=  (-Rough_table[i-1][0])

print("Routh Table:")
print(Rough_table)
if np.any(Rough_table[:,0] <= 0):
    print("The system is unstable")
else:
    print("The system is stable")