import numpy as np

# Solving the system of linear equations Ax = b
A = np.array([[1,0,0,0],
              [-2,1,1,0],
              [0,-2,-1,1],
              [0,0,0,-1]])

b = np.array([1,6,11,6])
x = np.linalg.solve(A,b)
print("The solution of the linear equations is:")
print(x)