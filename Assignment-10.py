import numpy as np

# Create 1D array from 21 to 30
arr = np.arange(21, 31)
print("Original Array:", arr)

# Slicing operations
first_five = arr[:5]
elements_step2 = arr[::2]

print("First 5 elements:", first_five)
print("Every second element:", elements_step2)

# Statistical measures
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Maximum:", arr.max())
print("Minimum:", arr.min())

# Broadcasting modification
arr_modified = arr + 5
print("Array after broadcasting (+5):", arr_modified)

'''
Output:
Original Array: [21 22 23 24 25 26 27 28 29 30]
First 5 elements: [21 22 23 24 25]
Every second element: [21 23 25 27 29]
Sum: 255
Mean: 25.5
Maximum: 30
Minimum: 21
Array after broadcasting (+5): [26 27 28 29 30 31 32 33 34 35]
'''