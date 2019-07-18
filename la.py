import numpy as np
from mat import *

A = readm('A.csv')
b = readm('b.csv')

def solve(A, b):
    # YOUR CODE HERE
    A,b  = np.array(A) , np.array(b)
    # 1. elimination
    n=len(A[0])
    x = np.array([0]*n)
    #print(f'n={n}')

    for k in range(n-1):   #pivot eq #k
        print(f'เลือกสมการที่={k}')
        for j in range(k+1,n):     #eliminate eq.#j
            print(f'\กำจัดตัวแปรที่{k},ออกจากสมการที่{j}')
            lam = A[j][k]/A[k][k]
            # update A[j][k เป็นต้นไป]
            A[j,k+1:n] = A[j,k+1:n] - lam*A[k,k+1:n]
            print(f'\t\tlamda={lam}')
            # update b[j]
            b[j] = b[j]-lam*b[k]
        #printm(A)
        #printm(b)
    
   
    for k in range(n-1,-1,-1):
        x[k] = (b[k]- np.dot(A[k,k+1:n],x[k+1:n]))/A[k,k]
    return x.flatten()
print( solve(A,b))
#print('===A===')
#printm(A)
#print('===b===')
#printm(b)
