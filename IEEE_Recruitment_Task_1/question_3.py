import numpy as np

mat = np.random.randint(1, 101, (5,5)) # initializes a random 5x5 matrix with ints ranging from 1 to 100

print("Matrix:")
print(mat)

print("Maximum: ", mat.max()) # finds and prints the max of the matrix
print("Minimum: ", mat.min()) # finds and prints the min of the matrix
print("Mean: ", mat.mean()) # finds and prints the mean of the matrix

mat = mat/mat.max() # normalizes the elements between 0 and 1 by dividing by the largest element
print("")
print("Normalized Matrix: ")
print(mat)


flatMat = mat.flatten() # flattens matrix into a 1D one
flatMat.sort() # sorts the flattened matrix
print("")
print("Flattened matrix: ")
print(flatMat)
