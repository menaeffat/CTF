#import numpy as np
import gmpy
import sympy as sp

def matrix_inv_mod(a,m):
    return modM(adj(a).applyfunc(lambda x:(x*det_inv(a,m))%m),m)

def adj(a):
    return a.adjugate()

def det(a):
    return a.det()

def det_inv(a,m):
    return mod_inv(int(det(a)%m),m)

def modM(a,m):
    return a.applyfunc(lambda x : x % m)

def mod_inv(d,m):
    return int(gmpy.invert(d,m))

def dot(a,b):
    A = sp.Matrix(a)
    B = sp.Matrix(b)
    return A*B

def dot_mod(a,b,m):
    return modM(dot(a,b),m)

##print("test...")
##
### A = C.D
### D = C-1.A
##
##c = sp.Matrix([[1,7],[3,4]])
##d = sp.Matrix([[3,20],[20,7]])
##a = c*d
##
##c_inv = matrix_inv_mod(c,29)
##d_f = modM(c_inv*a,29)
##
##print(d)
##print(d_f)
Q = 'KZTMQGKHW_'
L = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}'

def makeReadable(a,L):
    s = ''
    for i in range(a.rows):
        for j in range(a.cols):
##            print(i,j,j*a.rows+i)
            s +=L[a[j*a.rows+i]]
    return s

def take2(Q):
    return [Q[i:i+2] for i in range(0,len(Q),2)]
def makeMatrix(s):
    r = []
    for i in s:
        r.append([L.find(i)])
    return sp.Matrix(r)

def decrypt(Q,k_inv,L):
    res = ''
    for p in take2(Q):
        x = (modM(k_inv*makeMatrix(p),len(L)))
        res += makeReadable(modM(k_inv*makeMatrix(p),len(L)),L)
    return res
#C = K.M mod29
#K_inv = M.C_inv mod 29
#M = K_inv*C mod 29

c = sp.Matrix([[10,19],[25,12]])
m = sp.Matrix([[0,2],[18,22]])
c_inv = matrix_inv_mod(c,len(L))
k_inv = modM(m*c_inv,len(L))
##print(k_inv)

##m_f = modM(k_inv*c,29)
##print(m_f)

print(decrypt(Q,k_inv,L))
