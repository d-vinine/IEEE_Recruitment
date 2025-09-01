import numpy as np
 
mat = np.random.randint(1, 101, (5,5)) # initializes a random 5x5 matrix with ints ranging from 1 to 100
print("Matrix:")
print(mat)

submat = mat[1:4,1:4] # slicing the matrix to get the internal 3x3 matrix
print("\nSubmatrix:")
print(submat)

firstRow = submat[0] # gets the first row of the submatrix
lastCol = submat[:,-1] # gets the last col of the submatrix

print("\nDot of first row and last column:")
print(np.dot(firstRow, lastCol)) 
