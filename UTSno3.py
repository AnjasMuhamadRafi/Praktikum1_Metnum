import scipy
from scipy.linalg import lu, lu_factor, lu_solve
import numpy as np

# Definisikan matriks A
A = np.array([[2.0, -2.5, -3.2], [0, 5.0, -4.5], [5.5, -8.5, 2.0]])

# Definisikan vektor b
b = np.array([6.75, 10.15, 75.0])

# Solusi yang diberikan Lu dan b
P, L, U = lu(A)
lu, piv = lu_factor(A)
x = lu_solve((lu, piv),b)
print ('Matriks P :\n ',P)
print ('Matriks L :\n ',L)
print ('Matriks U :\n ',U)
print ('Solutions :\n ',x)