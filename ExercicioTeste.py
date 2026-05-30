

def swapSort(V):
    N = len(V)
    for i in range(0,N-1):
        for j in range(i+1,N):
            if(V[i] > V[j]):
                V[i],V[j] = V[j], V[i]
                
V = [1,5,3,8,6,4]
print(V)
swapSort(V)
print(V)
