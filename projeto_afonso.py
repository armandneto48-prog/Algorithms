import time
import random
import numpy as np
import matplotlib.pyplot as plt
import statistics


# =========================
# SORTS (os teus)
# =========================

def insertionSort(V):
    N = len(V)
    for j in range(1, N):
        key = V[j]
        i = j - 1
        while i >= 0 and V[i] > key:
            V[i + 1] = V[i]
            i -= 1
        V[i + 1] = key


def bubbleSort(V):
    j = 0
    ok = False
    N = len(V)
    while not ok:
        ok = True
        for i in range(N - 1, j, -1):
            if V[i - 1] > V[i]:
                V[i - 1], V[i] = V[i], V[i - 1]
                ok = False
        j += 1


def SelectionSort(V):
    N = len(V)
    for j in range(N - 1):
        min_idx = j
        for i in range(j + 1, N):
            if V[i] < V[min_idx]:
                min_idx = i
        V[j], V[min_idx] = V[min_idx], V[j]


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


def quickSort(V, i, f):
    if i < f:
        pivot = partition(V, i, f)
        quickSort(V, i, pivot - 1)
        quickSort(V, pivot + 1, f)


def partition(V, i, f):
    pivot = V[i]
    a = i
    for b in range(i + 1, f + 1):
        if V[b] <= pivot:
            a += 1
            V[a], V[b] = V[b], V[a]
    V[a], V[i] = V[i], V[a]
    return a


def quickSort2(V, i, f):
    if i < f:
        pivot = partition2(V, i, f)
        quickSort2(V, i, pivot - 1)
        quickSort2(V, pivot + 1, f)


def partition2(V, i, f):
    p = V[i]
    a = i
    b = f + 1
    while True:
        while True:
            a += 1
            if a > f or V[a] >= p:
                break
        while True:
            b -= 1
            if b < i or V[b] <= p:
                break
        if a >= b:
            break
        V[a], V[b] = V[b], V[a]
    V[b], V[i] = V[i], V[b]
    return b


def quickSort3(A, i, f):
    if i >= f:
        return
    k = random.randint(i, f)
    A[k], A[i] = A[i], A[k]
    me, ma = partition3(A, i, f)
    quickSort3(A, i, me - 1)
    quickSort3(A, ma + 1, f)


def partition3(A, i, f):
    pivot = A[i]
    menors = i
    x = i
    maiors = f

    while x <= maiors:
        if A[x] < pivot:
            A[menors], A[x] = A[x], A[menors]
            menors += 1
            x += 1
        elif A[x] > pivot:
            A[x], A[maiors] = A[maiors], A[x]
            maiors -= 1
        else:
            x += 1
    return menors, maiors


# =========================
# WRAPPERS (uniformizar chamadas)
# =========================

def ins_sort(A): insertionSort(A)
def bub_sort(A): bubbleSort(A)
def sel_sort(A): SelectionSort(A)

def shell_sort(A):
    gaps = [len(A)//2, len(A)//4, 1]
    shellSort(A, gaps)

def quick_sort(A): quickSort(A, 0, len(A)-1)
def quick_sort2(A): quickSort2(A, 0, len(A)-1)
def quick_sort3(A): quickSort3(A, 0, len(A)-1)


# =========================
# BENCHMARK
# =========================

def benchmark(sort_func):

    sizes = list(range(1, 101))
    times = []

    for n in sizes:

        data = random.sample(range(n * 10), n)

        start = time.perf_counter()
        sort_func(data)
        end = time.perf_counter()

        times.append(end - start)

    return sizes, times
# =========================
# PLOT
# =========================

def plot(sizes, times, title):

    plt.figure()
    plt.plot(sizes, times)

    plt.xlabel("n (número de elementos)")
    plt.ylabel("tempo (segundos)")
    plt.title(title)

    plt.show()


# =========================
# EXECUÇÃO FINAL
# =========================

algorithms = {
    "Insertion Sort": ins_sort,
    "Bubble Sort": bub_sort,
    "Selection Sort": sel_sort,
    "Shell Sort": shell_sort,
    "Quick Sort": quick_sort,
    "Quick Sort Hoare": quick_sort2,
    "Quick Sort 3-way": quick_sort3
}


for name, func in algorithms.items():

    print("A testar:", name)

    s, t = benchmark(func)

    plot(s, t, name)