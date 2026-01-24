import numpy as np

a_s = np.array([1,10,35,50,24])
row = len(a_s)
col = row//2 + row%2

print(row,col)

Rough_table = np.zeros((row, col), dtype=np.int32)
for i in range(2*col):
    if(i < row):
        Rough_table[i%2][i//2] = a_s[i]

print("Initial Routh Table:")
print(Rough_table)

for i in range(2,row):
    for j in range(col):
        print(i,j)
        if(j == col-1): # Last column
           Rough_table[i][j] = 0
        else:
           Rough_table[i][j] = Rough_table[i-2][0] * Rough_table[i-1][j+1] - Rough_table[i-2][j+1] * Rough_table[i-1][0]
           Rough_table[i][j] = -Rough_table[i][j] / Rough_table[i-1][0] if Rough_table[i-1][0] != 0 else 0

print("Routh Table:")
print(Rough_table)
if np.any(Rough_table[:,0] <= 0):
    print("The system is unstable")
else:
    print("The system is stable")