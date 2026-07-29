import time
import random

def insertionSort (V):
    N = len(V)
    for j in range(1,N):
        key = V[j]
        i = j - 1
        while (i >= 0 and V[i] > key):
	        V[i+1] = V[i];
	        i -= 1
        V[i+1] = key;



def bubbleSort (V):
    j=0
    ok=False
    N = len(V)
    while (not ok):
        ok = True
        for i in range(N-1,j,-1):
            if (V[i-1] > V[i]):
                #swap
                V[i-1], V[i] = V[i], V[i-1] 
                ok = False
        j += 1


def bubbleSort2(V):
    N = len(V)
    for i in range(N-1,0,-1):
        for j in range(0,i):
            if (V[j] > V[j+1]):
	            #swap
                V[j], V[j+1] = V[j+1], V[j] 



def swap(V, i, j):
    temp = V[i]
    V[i] = V[j]
    V[j] = temp

def swapSort(V):
    N = len(V)
    for i in range(0, N-1):
        for j in range(i+1, N):
            if(V[i] > V[j]):
                swap(V, i, j)




def SelectionSort(V):
	N = len(V)
	for j in range(0,N-1):
		min = j
		i = j + 1
		while(i < N):
			if(V[min] > V[i]):
				min = i
			i += 1
		if(j != min):
			V[j], V[min] = V[min], V[j]




def shellSort (V, gaps):
    N = len(V)
    for h in gaps:
        for i in range(h, N):
            key = V[i]
            j = i
            while( j >= h and V[j - h] > key ):
                V[j] = V[j - h]
                j -= h
            V[j] = key



# versao classica original
def mergeSort(V, i, f):
    if(i < f):    
        m = i + (f - i) // 2
        mergeSort(V, i, m,)
        mergeSort(V, m+1, f)
        merge(V, i, m, f)

def merge(V, i, m, f):
    n1 = m - i + 1
    n2 = f - m

    #fazer auxs e copiar V[] para eles
    N = [0] * n1
    M = [0] * n2
    for j in range(0, n1):
        N[j] = V[i + j]
    for j in range(0, n2):
        M[j] = V[m + 1 + j]

    #fusao  (a->idx de N[], b-> idx de M[], k->idx de V[])
    a = 0
    b = 0
    k = i
    while(a < n1 and b < n2):
        if(N[a] < M[b]):
            V[k] = N[a]
            a += 1
        else:
            V[k] = M[b]
            b += 1 
        k += 1
     
    # copiar resto dos arrays para V[]
    while a < n1:
        V[k] = N[a]
        k += 1
        a += 1
    while b < n2:
        V[k] = M[b]
        k += 1
        b += 1



# mergeSort mais simples
def mergeSort3(V):
    N = len(V)
    if(N <= 1):
        return V

    m = N // 2
    left  = V[:m]
    right = V[m:]

    return merge3( mergeSort3(left), mergeSort3(right) )

def merge3(left, right):
    result = []
    i = j = 0

    while( i < len(left) and j < len(right) ):
        if(left[i] < right[j]):
            result += [left[i]]
            i += 1
        else:
            result += [right[j]]
            j += 1

    return result + left[i:] + right[j:]



# assume que aux e inicalmente uma copia de V
def mergeSort2(V, aux, i, f):
    if(i < f):    
        m = i + (f - i) // 2
        mergeSort2(aux, V, i, m,)
        mergeSort2(aux, V, m+1, f)  # alterna nos papeis de aux[] e V[]
        merge2(V, aux, i, m, f)

def merge2(V, aux, i, m, f):

    #fusao
    a = i
    b = m + 1 
    for k in range(i,f+1): 
        if(a > m):
            aux[k] = V[b] 
            b += 1
        else:
            if(b > f):
                aux[k] = V[a] 
                a += 1
            else:
                if(V[b] < V[a]):
                    aux[k] = V[b]
                    b += 1
                else:
                    aux[k] = V[a]
                    a += 1
     


def quickSort (V, i, f):
    if(i < f):    
        pivot = partition(V,i,f)
        quickSort(V, i, pivot-1)
        quickSort(V, pivot+1, f)

# particao de Lomuto (mais simples)
def partition (V, i, f):
    # escolhar primeiro elemento do array dado como pivot
    pivot = V[i]
 
    # indice de elemento maior que pivot 
    a = i
 
    # travessia do array 
    # compara cada elemento com o pivot
    for b in range(i+1, f+1):
        if V[b] <= pivot:
 
            # se e' encontrado elemento menor que pivot
            # faz swap do maior elemento com indice i (referido por i)
            a = a + 1
 
            # Swapping  de indice a com indice b 
            (V[a], V[b]) = (V[b], V[a])
 
    # Swap do pivot com maior elemento que é referido por a 
    (V[a], V[i]) = (V[i], V[a])
 
    # retorna indice do pivot onde ocorre a particao.
    return a 

def quickSort2(V, i, f):
    if(i < f):    
        pivot = partition2(V,i,f)
        quickSort2(V, i, pivot-1)
        quickSort2(V, pivot+1, f)

# original de Hoare. produz melhores particoes (mais estaveis).
# tipicamente faz 3 x menos swaps que Lomuto...
def partition2(V, i, f):
    p = V[i]  # pivot no leftmost
    a = i
    b = f + 1
    # atravessar array e comparar com pivot
    while(True):
        while(True):
            a += 1
            if(a > f or V[a] >= p): break   # until
        while(True):
            b -= 1
            if(b < i or V[b] <= p): break  # until

        if(a >= b): break    # until
        V[a], V[b] = V[b], V[a]

    V[b], V[i] = V[i], V[b]
    return b      # retorna pos do pivot


# versao para 3 particoes: esq, pivots, direita
def quickSort3(A, i, f):
	if(i >= f):
		return
	k = random.randint(i, f) # escolhe pivot
	A[k], A[i] = A[i], A[k]
	me, ma = partition3(A, i, f)
	quickSort3(A, i, me - 1)
	quickSort3(A, ma + 1, f)


def partition3(A, i, f):       # particao ideal para listas com poucos duplicados
    menors = i       # menores que pivot
    x = i
    maiors = f       # maiores que pivot
    pivot = A[i]     # pivot ccomo o primeiro do array (random na funcao QS3)
    while (x <= maiors):      # a comecar no primeiro elemento
        if(A[x] < pivot):
            A[menors], A[x] = A[x], A[menors]
            menors += 1
            x += 1
        elif(A[x] > pivot):
            A[x], A[maiors] = A[maiors], A[x]
            maiors -= 1
        else:
            x += 1	
    return menors, maiors         # agora retorna dois indices!



def countingSort(A, N, k):   # assume-se que A[1..N]
    # faz array B[]
    B = [0]
    for i in range(1,N+1):
        B += [0]
    C = [0]
    for i in range(1,k+1):
        C += [0]

    for i in range(1,N+1):
        C[A[i]] += 1
    for i in range(1,k+1):  # acumulado!
        C[i] += C[i-1]
    for j in range(N,0,-1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1

    return B






# lista tam=N
def faz_lista(N,Gama):
    print("N="+str(N))
    V = []
    for i in range(1,N+1):  #   lista de N elementos (a variar nas vossas experiencias)
        V += [random.randrange(1,Gama+1)]  # gama de valores 
    return V


# programa principal
print()
print()

# gera lista
# Muito havera a fazer aqui... tipo de distribuicao, gama de valores, tamanho, ocorrencia de duplicados, etc...
V = faz_lista(1000,500)
print(V)


# benchmark
tot = 0.0
for i in range(1,100):
    A = V.copy()
    # podemos tentar com time.perf_counter()
    st = time.process_time()
    bubbleSort(A)
    en = time.process_time()
    tot += (en-st)
print("BS  time="+str(tot))

tot = 0.0
for i in range(1,100):
    A = V.copy()
    st = time.process_time()
    quickSort(A,0,len(A)-1)
    en = time.process_time()
    tot += (en-st)
print("QS  time="+str(tot))

tot = 0.0
for i in range(1,100):
    A = V.copy()
    st = time.process_time()
    A=mergeSort(A,0,len(A)-1)
    en = time.process_time()
    tot += (en-st)
print("MS  time="+str(tot))

tot = 0.0
for i in range(1,100):
    A = V.copy()
    aux = V.copy()
    st = time.process_time()
    A=mergeSort2(A,aux,0,len(A)-1)
    en = time.process_time()
    tot += (en-st)
print("MS2  time="+str(tot))

tot = 0.0
for i in range(1,100):
    A = V.copy()
    st = time.process_time()
    A=mergeSort3(A)
    en = time.process_time()
    tot += (en-st)
print("MS3  time="+str(tot))
# adicionar o resto....
