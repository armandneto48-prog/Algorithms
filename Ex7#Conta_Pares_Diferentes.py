def diferentes(V):
    
    N = len(V)
    diff = 0
    for i in range(0,N):
        j = i + 1
        while( j < N and V[i] == V[j]):
            j += 1
        if(j < N):
            diff += 1
    return diff

V = [3,4,1,7,3,4,7,10]

print(V)
diferentes(V)
print(V)