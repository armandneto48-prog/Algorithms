V=[1,6,9,24,5]

'''#EXERCICIO 1

    def maximo(V):
    r=V[0]
    N= len(V)
    for i in range(1,N):
        if V[i]>r:
            r=V[i]
    return r

print(maximo(V))'''

'''def maximo(V):
    r=V[0]
    N=len(V)
    i=0
    while i<N:
        if(V[i]>r):
            r=V[i]
        i=i+1
    return r

valorMax = maximo(V)
print(valorMax)'''

'''#EXERCICIO 3 - MULTIPLOS DE 3

N= int(input("Insira um número"))

def mult3(N):
    print("Múltiplos de 3 entre 1 e ", str(N))
    num = 1
    multiplos = ''
    for num in range (1,N+1):
        if(num%3 == 0):
            multiplos = multiplos + str(num) + ","
    print("Os múltiplos de 3 neste intervalo são: ", multiplos)

print(mult3(N))'''

#EXERCICIO 3 - ESCREVER OS NÚMEROS ATÉ AO PRIMEIRO NEGATIVO

V=[1,6,6,6,4,4,7,9,9,4,7,9,2,-6,0,3,10]

'''def ateAoNegativo(V):
    i=0
    print("Escrever os números não negativos:")
    while i<len(V) and V[i]>=0:
        print(V[i])
        i+=1
    else: 
        print("Encontrei um negativo! -", V[i])
        
print(ateAoNegativo(V))'''

'''def quantos(V):
    numero = int(input("Insira um número: "))
    menores = []
    maiores = []
    i=0
    
    for i in range (0,len(V)):
        if V[i]>=numero:
            maiores.append(V[i])
            i+=1
        else:
            menores.append(V[i])
            i+=1
    print(maiores, menores)

print(quantos(V))'''

'''def distintos(V):
    distintos = [V[0]]
    i=1
    
    for i in range (1,len(V)):
        if V[i] not in (distintos):
            distintos.append(V[i])
    print(distintos)
    
print(distintos(V))'''

'''S="relogio"

def palin (S):
    i = 0
    t= len(S)
    
    while i<t:
        if S[i] == S[t-1]:
            i+=1
            t-=1
        else:
            return False
    return True
            
print(palin(S))'''

S=7
def soma(V,S):
    pares=[]
    
    for i in range (0,len(V)):
        for x in range (1, len(V)-1):
            if V[i]+V[x]==S and ((V[i],V[x]) not in pares):
                pares.append((V[i],V[x]))
    return pares
print(soma(V,S))

        
        






        
    
        