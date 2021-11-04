import numpy as np
import sys


n = int(input('Masukan jumlah variabel: '))


# Membuat array berukuran n x n+1 dan menginisiasi
# Menyimpan matriks augmente A|b
a = np.zeros ((n,n+1))

# Membuat array berukuran n dan menginisiasi
# Vektor solusi
x = np.zeros(n)

# Membaca koefisien matriks augmented
print('Masukkan koefisien matriks augmented:')
for i in range(n):
    for j in range (n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+str(j)+']='))

# Implementasi Elimanasi Gauss Jordan
for i in range (n):
    if a[i][i] == 0.0:
        sys.exit('Devide by zero detected!')

    for j in range(n):
        if i !=j:
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

# Penentuan Solusi
for i in range(n):
    x[i] = a[i][n]/a[i][i]

# Menampilkan Solusi
print('\nSolusi yang dibutuhkan: ')
for i in range(n):
    print('X%d = %0.6f' %(i,x[i]), end = '\t')   