# Reshaping and Broadcasting Techniques
# Reshaping :- Changing the shape of an array without changing its data.
# Broadcasting :- A powerful mechanism that allows NumPy to work with arrays of different shapes during arithmetic

#--------------------------------------------------
#1. Reshaping 
#--------------------------------------------------

import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5, 6])
print("\n\nOriginal 1D Array :")
print(arr_1d)
print("Shape of Original 1D Array :", arr_1d.shape)

# Reshaping to a 2D array (2 rows, 3 columns)

arr_2d = arr_1d.reshape(2, 3)
print("\n\nReshaped to 2D Array (2 rows, 3 columns) :")
print(arr_2d)
print("Shape of Reshaped 2D Array :", arr_2d.shape)

# Reshaping to a 3D array (2 blocks, 1 row, 3 columns)

arr_3d = arr_1d.reshape(2, 1, 3)
print("\n\nReshaped to 3D Array (2 blocks, 1 row, 3 columns) :")
print(arr_3d)
print("Shape of Reshaped 3D Array :", arr_3d.shape)


#--------------------------------------------------
#2. Broadcasting 
#--------------------------------------------------

# Creating two arrays of different shapes

array_a = np.array([[1, 2, 3],
                    [4, 5, 6]])

array_b = np.array([10, 20, 30])
print("\n\nArray A :")
print(array_a)
print("\n\nArray B :")
print(array_b)

# Adding the two arrays using broadcasting

result = array_a + array_b
print("\n\nResult of Adding Array A and Array B using Broadcasting :")
print(result)

# Creating another array with a different shape

array_c = np.array([[100],
                    [200]])
print("\n\nArray C :")
print(array_c)

# Adding Array A and Array C using broadcasting

result2 = array_a + array_c
print("\n\nResult of Adding Array A and Array C using Broadcasting :")
print(result2)

# Multiplying Array A and Array B using broadcasting

result3 = array_a * array_b
print("\n\nResult of Multiplying Array A and Array B using Broadcasting :")
print(result3)

# Verifying the shapes of the arrays involved in broadcasting

print("\n\nShape of Array A :", array_a.shape)
print("Shape of Array B :", array_b.shape)
print("Shape of Array C :", array_c.shape)
print("Shape of Result (A + B) :", result.shape)
print("Shape of Result (A + C) :", result2.shape)
print("Shape of Result (A * B) :", result3.shape)
