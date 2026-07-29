import time
import matplotlib.pyplot as plt
import random

def shellSort(V, gaps):
    N = len(V)
    for h in gaps:
        for i in range(h, N):
            key = V[i]
            j = i
            while j >= h and V[j - h] > key:
                V[j] = V[j - h]
                j -= h
            V[j] = key




# --- Análise de Performance ---
tamanhos = [1000, 5000, 10000]
tempos = []

for n in tamanhos:
    lista_teste = [random.randint(0, 10000) for _ in range(n)]
    # Experimenta estas duas variações e vê o gráfico divergir:
    gaps = [n(//2, n//4)]

    
    inicio = time.time()
    shellSort(lista_teste, gaps)
    fim = time.time()
    
    tempos.append(fim - inicio)

# Criando o Gráfico
plt.plot(tamanhos, tempos, marker='o', label='Shell Sort')
plt.title('Complexidade Temporal - Shell Sort')
plt.xlabel('Tamanho da Lista (N)')
plt.ylabel('Tempo (segundos)')
plt.grid(True)
plt.show()
