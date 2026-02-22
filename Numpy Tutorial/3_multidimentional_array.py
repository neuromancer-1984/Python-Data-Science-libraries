import numpy as np

array = np.array([[['A','B','C'],
                  ['D','E','F'],
                  ['G','H','I']],
                  [
                  ['I','J','K'],
                  ['L','M','N'],
                  ['O','P','Q'],
                  ['R','S','T']],
                  [['U','V','W'],
                  ['X','Y','Z'],
                  ['I','J','K']]])

print(array.ndim)
print(array.shape)

print(array)

print(array[0,0,0]+array[1,1,1]+array[2,2,2])
print(array[1,1,1])