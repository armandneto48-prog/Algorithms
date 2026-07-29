
# ex1 Algoritmo Iterativo:

A = [1,2,5,0,2,4,6,7,3,2,10,8]

def faz_algo(A): 

    N = len(A)
    m = A[0]
    conta = 1
    for i in range(1,N):
        if(A[i] > m):
            m = A[i]
            conta += 1

    return conta

a = faz_algo(A)

print(a)



# e2 Algoritmo de Ordenação

def multiplos(A):

    N = len(A)
    conta = 0
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            if(A[j] % A[i] == 0):
                conta += 1
    return conta

# ex3 Algoritmo Recursivo:

def maxInt(A,i,f):

    if(i>=f):
        return A[i]
    
    m = int( (f+i)/2)
    l = maxInt(A,0,m)
    r = maxInt(A, m + 1, f)
    if(l > r):
        return 1
    else:
        return r
