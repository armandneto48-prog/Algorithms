

def repetidos(V):
    N = len(V)
    for i in range(0,N-1):
        for j in range(i+1,N):
            if(V[i] == V[j]):
                return(True)
    return False

V = [1,6,34,7,2,89,4,6]
print(V)
repetidos(V)
print(V)

