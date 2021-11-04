import numpy as np
import matplotlib.pyplot as plt
from math import e, sin #Untuk memanggil bilangan eksponen natural (e)

# Mendefinisikan fungsi
def f(x):
  return sin (1)/x
  
# Mendefinisikan turunan fungsi
def Df(x):
    return 1

# Metode Newthon-Rapshon
def newtonRaphson(a,b,eps):
    step = a
    print('\n\n*** ---METODE NEWTON RAPSHON--- ***')
    xn = a
    for n in range(0,100): 
        fxn=f(xn)
        if abs(fxn) < eps:
            print('\n Akar Persamaan tersebut : %0.8f' % xn)
            return xn
        Dfxn=Df(xn)
        if Dfxn == a:
            print('Solusi tidak ditemukan')
            return None
        xn=xn-(fxn/Dfxn)
        step = step + 1
        print('Iterasi-%d, x = %0.8f dan f(x) = %0.8f' % (step, xn, f(xn)))
    print('Iterasi maksimum, solusi tidak ditemukan')

# Sesi Input Nilai Awal yang dikonversi ke pecahan
a = float(input('a: '))
b = float(input('b: '))
eps = float(input('epsilon : '))
newtonRaphson(a,b,eps)