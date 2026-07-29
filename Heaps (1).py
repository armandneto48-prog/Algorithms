# Heaps e suas operacoes
# Heapsort e construcao de min-heaps

def bubble_up(V, i):
	p = int((i - 1) / 2)   # antecessor de i
	while(i > 0 and V[i] < V[p]):
		V[i], V[p] = V[p], V[i]   # swap
		i = p
		p = int((i - 1) / 2)  # antecessor de i

def bubble_down(V, N, i):
	f = 2*i + 1   # sucessor de i
	flag = False
	while(f < N and not flag):
		 # descendente da direita e menor?
		if(f+1 < N and V[f+1] < V[f]):
			f = f + 1
		if(V[f] > V[i]): 
			flag = True
		else:
			V[i], V[f] = V[f], V[i]  # swap
			i = f
			f = 2*i + 1   # sucessor de i

def heapify(V,N):
    for i in range(1,N):
        bubble_up(V,i)

def heapSort(V):
    N = len(V)
    heapify(V,N)
    for i in range(N-1,-1,-1):
        V[0], V[i] = V[i], V[0]
        bubble_down(V,i,0)

# main prog
A = [22,18,16,13,11,8,6,5,4,3,30,26]
print(A)
print("heapify")
heapify(A,len(A))
print(A)
print()
print()
A = [18,16,26,13,11,8,6,30,5,4,22,3]
heapSort(A)
print("HeapSort")
print(A)
print()

A = [2, 9, 7, 6, 5, 8]
print(A)
print("HeapSort")
heapSort(A)
print(A)

print()
A=[11,20,14,12,25,30,10,23,19]
print(A)
print("heapify")
heapify(A,len(A))
print(A)
print(" remove 10  --  bubble down")
A[0]=A[len(A)-1]
A[len(A)-1]='-'
bubble_down(A,len(A)-1,0)
print(A)
