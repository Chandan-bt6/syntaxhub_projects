import numpy as np
import time

# =====================================================
# COMPARING NUMPY PERFORMANCE WITH PYTHON LISTS
# =====================================================

# Creating large datasets
size = 1000000

python_list = list(range(size))
numpy_array = np.arange(size)

# =====================================================
# PYTHON LIST PERFORMANCE
# =====================================================

start_time = time.time()

python_result = [x * 2 for x in python_list]

end_time = time.time()

python_time = end_time - start_time

print("Python List Operation Time:")
print(python_time, "seconds")

# =====================================================
# NUMPY ARRAY PERFORMANCE
# =====================================================

start_time = time.time()

numpy_result = numpy_array * 2

end_time = time.time()

numpy_time = end_time - start_time

print("\nNumPy Array Operation Time:")
print(numpy_time, "seconds")

# =====================================================
# PERFORMANCE COMPARISON
# =====================================================

print("\nPerformance Comparison:")

if numpy_time < python_time:
    print("NumPy is faster than Python Lists!")
else:
    print("Python Lists are faster!")

# =====================================================
# MEMORY COMPARISON
# =====================================================

print("\nMemory Comparison:")

print("Python List Size:",
      len(python_list) * python_list[0].__sizeof__(),
      "bytes")

print("NumPy Array Size:",
      numpy_array.nbytes,
      "bytes")

# =====================================================
# PROJECT CONCLUSION
# =====================================================

print("\nConclusion:")
print("NumPy provides faster computation and better")
print("memory efficiency compared to standard Python lists.")