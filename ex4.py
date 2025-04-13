# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating a NumPy array 'x' containing elements 1, 0, 0, and 0
x = np.array([1, 0, 0, 0])

# Printing the original array 'x'
print("Original array:")
print(x)

# Checking if any element in the array 'x' is non-zero and printing the result
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x))

# Reassigning array 'x' to a new array containing all elements as zero
x = np.array([0, 0, 0, 0])

# Printing the new array 'x'
print("Original array:")
print(x)

# Checking if any element in the updated array 'x' is non-zero and printing the result
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x)) 
