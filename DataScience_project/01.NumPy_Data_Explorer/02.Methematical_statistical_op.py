# Mathematical axis-wise operations
# Statistical axis-wise operations

#  [[1 , 2  , 0 , 4], ->   row 0
#  [ 4 , 0.5, 6 , 0], -> row 1
#  [2.6,  0 , 7 , 8], -> row 2
#  [3  ,  7 , 4 ,2.0]])  -> row 3
#   |     |   |   |
#   c0   c1  c2  c3

# -----------------------------------------------
# AXIS UNDERSTANDING
# ------------------------------------------------

# axis = 0  → column wise operation
# axis = 1  → row wise operation

#------------------------------------------------

import numpy as np

# Creating a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("\n\nOriginal Array :")
print(arr)

#---------------------------------------------------------------
#1. Mathematical axis-wise operations
#---------------------------------------------------------------

# Sum along columns (axis = 0)
col_sum = np.sum(arr,axis = 0)
print("\n\nSum along columns (axis=0) :")
print(col_sum)

# # Sum along rows (axis = 1)
# row_sum = np.sum(arr,axis = 1)
# print("\n\nSum along rows (axis=1) :")
# print(row_sum)

# Mean along columns (axis = 0)
col_mean = np.mean(arr,axis = 0)
print("\n\nMean along columns (axis=0) :")
print(col_mean)

# Mean along rows (axis = 1)
row_mean = np.mean(arr,axis = 1)
print("\n\nMean along rows (axis=1) :")
print(row_mean)

#---------------------------------------------------------------
#2. Statistical axis-wise operations
#---------------------------------------------------------------

# Standard deviation along columns (axis = 0)
col_std = np.std(arr,axis = 0)
print("\n\nStandard deviation along columns (axis=0) :")
print(col_std)


# Variance along columns (axis = 0)
col_var = np.var(arr,axis = 0)
print("\n\nVariance along columns (axis=0) :")
print(col_var)

# Median along rows (axis = 1)
row_median = np.median(arr,axis = 1)
print("\n\nMedian along rows (axis=1) :")
print(row_median)

# Minimum along columns (axis = 0)
col_min = np.min(arr,axis = 0)
print("\n\nMinimum along columns (axis=0) :")
print(col_min)

# Maximum along rows (axis = 1)
row_max = np.max(arr,axis = 1)
print("\n\nMaximum along rows (axis=1) :")
print(row_max)

#----------------------------------------------------------------
#3. Index based axis-wise operations
#----------------------------------------------------------------

# Index of minimum along columns (axis = 0)
col_index_min = np.argmin(arr,axis = 0)
print("\n\nIndex of minimum along columns (axis=0) :")
print(col_index_min)

# Index of maximum along rows (axis = 1)
row_index_max = np.argmax(arr,axis = 1)
print("\n\nIndex of maximum along rows (axis=1) :")
print(row_index_max)