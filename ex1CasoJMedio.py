V = [3,1,2,3,9,4,7]

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