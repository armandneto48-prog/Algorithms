# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 11:16:29 2025

@author: Asus
"""

V = [4, 4, 6, 7, 1, 2]
a = 0
b = 4

def dup2(V, a, b):
    # Caso base: quando a atingir b, termina a recursão
    if a == b:
        return
    
    # Comparar V[a] com os próximos elementos de V
    for j in range(a + 1, b):
        if V[a] == V[j]:
            print(f"{V[a]} e {V[j]} são duplicados")
    
    # Recursão: avançar para o próximo elemento
    dup2(V, a + 1, b)

# Chamada inicial
dup2(V, a, b)
    