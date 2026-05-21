# Numpy Fundamentals Example

import numpy as np
#--------------------------------------------------------------
#1. Array Creation
#------------------------------------------------------

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("\n\n 1D Array :")
print(arr1)

# Creating a 2D array
arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])        
print("\n\n 2D Array :")
print(arr2)

#--------------------------------------------------------------
#2. Indexing 
#--------------------------------------------------------------

# Accessing elements in a 2D array
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("\n\nOriginal Array :")
print(arr)

# Accesing elements from 1D array using indexing
print("\n\nElement at index 2 in 1D array :")
print(arr1[2])

# Accesing elements from 2D array using indexing
print("\n\nElement at (2,1) :")
print(arr[2][1])

#---------------------------------------------------------------
#3. Slicing
#---------------------------------------------------------------

# Slicing a 1D array
print("\n\nSlicing 1D array from index 1 to 4: ")
print(arr[1:4])

# Slicing a 2D array
print("\n\nSlicing 2D array (first two rows): ")
print(arr[:2, :])

#----------------------------------------------------------------
#4. Reshaping
#---------------------------------------------------------------

# Reshaping a 1D array to 2D
reshaped_arr = arr1.reshape(5,1)
print("\n\nReshaped 1D array to 2D (5,1): ")
print(reshaped_arr)

# Reshaping a 2D array to 1D
flatten_arr = arr2.flatten()
print("\n\nFlattened 2D array to 1D: ")
print(flatten_arr)

# 