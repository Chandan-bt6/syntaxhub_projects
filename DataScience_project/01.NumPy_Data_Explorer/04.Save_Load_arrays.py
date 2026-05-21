import numpy as np

# =====================================================
# NUMPY SAVE / LOAD OPERATIONS PROJECT
# =====================================================

# Creating NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])

arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


print("Original Array 1:")
print(arr1)

print("\nOriginal Array 2:")
print(arr2)

# =====================================================
# 1. SAVE SINGLE ARRAY USING .npy FORMAT
# =====================================================

np.save("array1.npy", arr1)

print("\narray1.npy file saved successfully!")

# =====================================================
# 2. LOAD SINGLE ARRAY
# =====================================================

loaded_arr1 = np.load("array1.npy")

print("\nLoaded Array 1:")
print(loaded_arr1)

# =====================================================
# 3. SAVE MULTIPLE ARRAYS USING .npz FORMAT
# =====================================================

np.savez("multiple_arrays.npz", first=arr1, second=arr2)

print("\nmultiple_arrays.npz file saved successfully!")

# =====================================================
# 4. LOAD MULTIPLE ARRAYS
# =====================================================

loaded_data = np.load("multiple_arrays.npz")

print("\nLoaded First Array:")
print(loaded_data['first'])

print("\nLoaded Second Array:")
print(loaded_data['second'])

# =====================================================
# 5. SAVE ARRAY AS TEXT FILE
# =====================================================

np.savetxt("array_text.txt", arr2, fmt='%d')

print("\narray_text.txt file saved successfully!")

# =====================================================
# 6. LOAD ARRAY FROM TEXT FILE
# =====================================================

loaded_text_array = np.loadtxt("array_text.txt")

print("\nLoaded Array From Text File:")
print(loaded_text_array)

# =====================================================
# PROJECT COMPLETED
# =====================================================

print("\nNumPy Save/Load Operations Completed Successfully!")