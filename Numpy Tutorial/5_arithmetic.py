import numpy as np
#Scalar Arithmetic
array  = np.array([1, 2, 3])

# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 4)
# print(array % 5)
# print(array ** 6)

# print(np.sqrt(array))

array1  = np.array([1.01, 2.56, 3.78])

# print(np.round(array1))

# print(np.pi)

# Vector Arithmetic

# radii = np.array([1,2,3])

# print(np.pi * (radii**2))

array101 = np.array([1,2,3])
array102 = np.array([4,5,6])

# print(array101 + array102)
# print(array101 / array102)

scores = np.array([91, 55, 100, 73, 82, 64])

# print(scores == 100)
# print(scores >= 60)

scores[scores < 60] = 0
print(scores)

