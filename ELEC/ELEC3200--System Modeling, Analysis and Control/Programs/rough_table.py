import numpy as np

# This is the input characteristic polynomial coefficients array
# For example, the polynomial is 3s^4 + 3s^3 + 9s^2 + 3s + 5
# If some coefficients are symbolic, please let the symbolic coefficients be 1000
a_s = np.array([3,3,9,3,5])
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
        print(f"Calculating Rough_table[{i}][{j}]:")
        print(f"numerator: {-Rough_table[i][j]}")
        print(f"denominator: {Rough_table[i-1][0]}")
        if Rough_table[i-1][0] != 0:
            Rough_table[i][j] /=  (-Rough_table[i-1][0])

print("Routh Table:")
print(Rough_table)
if np.any(Rough_table[:,0] <= 0):
    print("The system is unstable")
else:
    print("The system is stable")