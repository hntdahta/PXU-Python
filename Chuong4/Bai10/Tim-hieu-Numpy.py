import numpy as np

vector = np.array([1, 2, 3, 4, 5])
print(vector)

mx5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
print(mx5)

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
B = np.array([[13, 14, 15, 16, 17], [16, 17, 18, 19, 20], [19, 20, 21, 22, 23], [22, 23, 24, 25, 26]])
C = A.dot(B)
print(C)

D = C.transpose()
print(D)