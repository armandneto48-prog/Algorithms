

"""1. Considere a seguinte função de calculo de máximo num array:

a) corrija a função por forma a não repetir processamento de elementos
de V;


b) Conte quantas vezes o ciclo for() é executado;


c) Altere a função anterior por forma a substituir o ciclo for() por um
ciclo while()."""

# () [] {} -> curly brackets

# Pergunta chave: O que este algoritmo faz?

V = [1,2,3,4]

def maximo(V):

    r = V[0] # agrega valor à variável r a partir da contagem do primeiro elemento de V
    
    N = len(V) # atribui-se o valor do tamanho do array 
    
    for i in range(1,N): # o ciclo for percorre desde o elemento i a N:

        # Possível resolução do problema? R: range(1,N)
        
        if(V[i] > r): # se o valor que a variável i tiver for maior que o primeiro elemento
            
            r = V[i] # iguala-se tal variável ao elemento

    return r



a = maximo(V)

# Resultado: o algoritmo busca fazer uma contagem cíclica de um array de inteiros.

print(a)


def maximo(V):

    r = V[0] # agrega valor à variável r a partir da contagem do primeiro elemento de V
    
    N = len(V) # atribui-se o valor do tamanho do array 
    
    i = 1

    while(i < N):

            if(V[i] > r):
                 
                 r = V[i]
            i += 1 
    
    return r



a = maximo(V)

# Resultado: o algoritmo busca fazer uma contagem cíclica de um array de inteiros.

print(a)


# ex2:

"""2. Assumindo que a e b são booleanos calcule o valor de seguinte expressão
lógica:

"""

a = (not (a and b) and (a or b)) or ((a and b) or not (a or b))
print(a)


# ex3 Corrija : 

num = 3

def printa_mult3(N): # Cria uma função baseada no tamanho do array N

    print("multiplos de 3 entre 1 e "+str(N)) # Gera o output e
    
    # soma-se com o dado inicial em forma de string

    for num in range(1, N + 1): # Contabiliza entre 1 a N + 1

        if(num % 3 != 0): # agrega-se um valor à variável igual a qualquer dado

            continue
print(num)



"""def ateAoNeg(V):  # escreve os números ate ao primeiro negativo

for num in V:
    if num < 0:
        break

print(f" encontrei um negativo: {num}. ")

print(num)



def mediana (V,N):

for i in range(0,N):

    m, M = quantos (V,V[i])

if(m <= N/2) and (M <= N/2):

    break

return V[i]"""