import time
import random
import statistics

#------------------INSERTION SORT-----------------------------------
#----> vai colocando os números na posição certa mediante a key em cada iteração

def insertionSort (V):
    N = len(V)
    for j in range(1,N):
        key = V[j]
        i = j - 1
        while (i >= 0 and V[i] > key):
	        V[i+1] = V[i];
	        i -= 1
        V[i+1] = key;

#-----------------BUBBLE SORT----------------------------------------
#-----> vai comparando os pares, faz iterações até ficar tudo ordenado

#bubbleSort1 - verifica se há trocas, se deixarem de haver, pára mais cedo
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
                
                
#--------------------SHELL SORT----------------------------------
#------uso de gaps

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

#--------------------MERGE SORT----------------------------------
#1º divide e depois junta de forma ordenada

#principal - vai dividindo
def mergeSort(V, i, f):
    if(i < f):    
        m = i + (f - i) // 2
        mergeSort(V, i, m,)
        mergeSort(V, m+1, f)
        merge(V, i, m, f)

#subfunção - com arrays auxiliares
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
        
#otimizada - alterna nos papéis de aux[] e V[]

def mergeSort2(V, aux, i, f):
    aux= [0]*len(V)
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
                    
#-------------------QUICK SORT----------------------------------
#ordena durante a partição

#VERSÃO 1 - COM PARTIÇÃO DE LOMUTO (MAIS SIMPLES)

def quickSort (V, i, f):
    if(i < f):    
        pivot = partition(V,i,f)
        quickSort(V, i, pivot-1)
        quickSort(V, pivot+1, f)

def partition (V, i, f):
    #elemento mais à direita como pivô
    pivot = V[i]
    # posição do maior elemento
    a = i
    
    # compara cada elemento com o pivô
    for b in range(i+1, f+1):
        if V[b] <= pivot:
 
            # se elemento inferior ao pivô, faz swap com elemento maior(a)
            a = a + 1
            (V[a], V[b]) = (V[b], V[a])
 
    # Swap do pivô com o elemento superior apontado por a
    (V[a], V[i]) = (V[i], V[a])
 
    # Return da posição onde se fez a partição
    return a 


#--VERSÃO 2 - PARTIÇÃO DE HOARE - PARTIÇÕES MAIS ESTÁVEIS, 3X MENOS SWAPS
def quickSort2(V, i, f):
    if(i < f):    
        pivot = partition2(V,i,f)
        quickSort2(V, i, pivot-1)
        quickSort2(V, pivot+1, f)

def partition2(V, i, f):
    p = V[i]  
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

#---VERSÃO 3
#ESCOLHA ALEATÓRIA DO PIVÔ
#ideal para listas com poucos duplicados
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

#-----------------COUNTING SORT---------------------------------

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

#--------------------------------------------------------------
###############################################################

def gerarLista(a,b):
    V=[]
    for i in range(1,a):  #   lista de 1000 elementos (a variar nas vossas experiencias)
        V += [random.randrange(1,b)]  # gama de valores em [1,500]
    return V
#gerados 4 arrays, com dimensão cada vez maior. V3 com duplicados
V1 = gerarLista(101,100)
V2= gerarLista(1001,1000)
V3 = gerarLista(1001,101)


gaps = [701,301,132,57,23,10,4,1]

def estatisticaAlgoritmos(tempos):
    media = statistics.mean(tempos)
    mediana = statistics.median(tempos)
    minimo = min(tempos)
    maximo = max(tempos)
    q1 = statistics.quantiles(tempos, n=4)[0]
    q3 = statistics.quantiles(tempos, n=4)[2]

    return {
        "média": media,
        "\n mediana": mediana,
        "\n mínimo": minimo,
        "\n máximo": maximo,
        "\n Q1": q1,
        "\n Q3": q3
    }


def testarAlgoritmo(nome, func, V, *args):
    tempos = []
    for _ in range(1, 100):
        A = V.copy()
        st = time.process_time()
        func(A, *args)
        en = time.process_time()
        tempos.append(en - st)
    print(f"\nDuração total do {nome} = {sum(tempos):.6f} segundos")
    print(estatisticaAlgoritmos(tempos))
    


def cronometro(V):
    f = len(V) - 1
    aux = [0] * len(V)

    testarAlgoritmo("bubbleSort1 (otimizado)", bubbleSort, V)
    testarAlgoritmo("bubbleSort2", bubbleSort2, V)
    testarAlgoritmo("InsertionSort", insertionSort, V)
    testarAlgoritmo("ShellSort", shellSort, V, gaps)
    testarAlgoritmo("MergeSort", mergeSort, V, 0, f)
    testarAlgoritmo("MergeSort2", mergeSort2, V, aux, 0, f)
    testarAlgoritmo("QuickSort", quickSort, V, 0, f)
    testarAlgoritmo("QuickSort2", quickSort2, V, 0, f)
    testarAlgoritmo("QuickSort3", quickSort3, V, 0, f)


cronometro(V2)

    
        

    
    
    
    
        
    