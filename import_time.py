import time
import matplotlib.pyplot as plt
import random
import numpy as np # Opcional: facilita a geração de intervalos

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

# --- Configuração da Experiência ---
# Geramos 20 pontos entre 100 e 10.000 para ver a "curva" se formar
tamanhos = np.linspace(100, 10000, 20, dtype=int)
tempos = []

print("A processar amostras...")
for n in tamanhos:
    # Gerar lista aleatória
    lista_teste = [random.randint(0, 10000) for _ in range(n)]
    
    # Sequência de Shell clássica
    gaps = []
    h = n // 2
    while h > 0:
        gaps.append(h)
        h //= 2
    
    inicio = time.perf_counter() # Mais preciso que time.time() para intervalos curtos
    shellSort(lista_teste, gaps)
    fim = time.perf_counter()
    
    tempos.append(fim - inicio)
    print(f"N={n} concluído.")

# --- Visualização Científica ---
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos, 'o-', color='blue', label='Shell Sort (Experimental)')

# Para "brincar", vamos plotar uma curva teórica N*log2(N)^2 para comparar
# Apenas para fins visuais de escala
escala = tempos[-1] / (tamanhos[-1] * (np.log2(tamanhos[-1])**2))
curva_teorica = [escala * (x * (np.log2(x)**2)) for x in tamanhos]
plt.plot(tamanhos, curva_teorica, '--', color='red', label='Tendência Teórica O(N log² N)')

plt.title('Análise Temporal Detalhada - Shell Sort')
plt.xlabel('Tamanho da Lista (N)')
plt.ylabel('Tempo de Execução (segundos)')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.show()