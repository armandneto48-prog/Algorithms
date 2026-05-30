# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 11:57:03 2025

@author: Asus
"""

V=[2,2,4,5,6,7,8]

'''def repetidos(V):
    N=len(V)
    for i in range(0, N-1):
        for j in range(i+1,N):
            if(V[i]==V[j]):
                return True
    return False
    
print(repetidos(V))'''

def soma(V,a):
    r=V[0]
    N=len(V)
    for i in range (1,N-1):
        if r< V[i] + V[i+1<N-1]:
            r=r+V[i+2<N-1]
    return r

def arrayNovo(V):
    N=len(V)
    array=V
    soma=array[0]
    maximo=0
    
    
    for i in range (1,N-1):
        soma+=V[i]
        if soma>maximo:
            maximo=soma
            array[i]=maximo
        else:soma-=V[i]
    return array

#print(arrayNovo(V))

x=20
y=3

def mult2(x,y):
    a=x
    b=y
    r=0
    while(a>0):
        if int(a%2)==1:
            r+=b
            a//=2
            b*=2
    return r


print(mult2(x,y))