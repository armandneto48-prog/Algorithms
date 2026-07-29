class NoAVL:
	 # construtor
	def __init__(self, valor=None, bal = 0, esq=None, dir=None):
		self.valor = valor
		self.esq = esq
		self.dir = dir
		self.bal = bal # deve ser 1, 0, ou -1 para balanceado!

def RotateRight(A):
	B = A.esq
	A.esq = B.dir
	B.dir = A
	return B

def RotateLeft(B):
	A = B.dir
	B.dir = A.esq
	A.esq = B
	return A

def fixRight(A):
    B = A.dir
    if(B.bal == -1):   # RIGHT
        A.bal = B.bal = 0 # BAL
        A = RotateLeft(A)
    else:
        C = B.esq
        match C.bal:
            case  1:
                A.bal = 0
                B.bal = -1 #RIGHT
            case -1: 
                A.bal = 1  #LEFT
                B.bal = 0
            case  0: 
                A.bal = B.bal = 0
        C.bal = 0
        A.dir = RotateRight(B)
        A = RotateLeft(A)
    return A

def fixLeft(A):
    B = A.esq
    if(B.bal == 1):   # LEFT
        A.bal = B.bal = 0 # BAL
        A = RotateRight(A)
    else:
        C = B.dir
        match C.bal:
            case  1:
                A.bal = -1 #RIGHT
                B.bal = 0
            case -1: 
                A.bal = 0  
                B.bal = 1 #LEFT
            case  0: 
                A.bal = B.bal = 0
        C.bal = 0
        A.esq = RotateLeft(B)
        A = RotateRight(A)
    return A


def insAVL(raiz, vals, cresce):
    if(raiz is None):
        return True, NoAVL(vals,0)
    else:
        if(raiz.valor > vals):
            cresce, raiz.esq = insAVL(raiz.esq, vals, cresce)
            if(cresce):
                match raiz.bal: 
                    case 1: #LEFT 
                        raiz = fixLeft(raiz)
                        cresce = False
                    case 0: 
                        raiz.bal = 1 # LEFT
                    case -1: #RIGHT 
                        raiz.bal = 0 # BAL
                        cresce = False
        else:
            cresce, raiz.dir = insAVL(raiz.dir, vals, cresce)
            if(cresce):
                match raiz.bal: 
                    case -1: #RIGHT 
                        raiz = fixRight(raiz)
                        cresce = False
                    case 0: 
                        raiz.bal = -1 # RIGHT
                    case 1: #LEFT
                        raiz.bal = 0  # BAL
                        cresce = False
    return cresce, raiz

# versao standard de BST
class No:
	 # construtor
	def __init__(self, valor=None, esq=None, dir=None):
		self.valor = valor
		self.esq = esq
		self.dir = dir

def insOrd(raiz, val):
	if( raiz is None):
		return No(val)
	if(raiz.valor > val):
		raiz.esq = insOrd(raiz.esq, val)
	else:
		raiz.dir = insOrd(raiz.dir, val) 
	return raiz


def in_ordem(raiz, exp):
	if( raiz is None):
		return exp
	esquerda = in_ordem(raiz.esq, exp)
	direita  = in_ordem(raiz.dir, exp)
	return exp + esquerda + [raiz.valor] + direita

def pre_ordem(raiz, exp):
	if( raiz is None):
		return exp
	esquerda = pre_ordem(raiz.esq, exp)
	direita  = pre_ordem(raiz.dir, exp)
	return exp + [raiz.valor] + esquerda + direita

# main
b, raiz = insAVL(None,5,False)
b, raiz = insAVL(raiz,1,b)
b, raiz = insAVL(raiz,6,b)
b, raiz = insAVL(raiz,7,b)
b, raiz = insAVL(raiz,10,b)
b, raiz = insAVL(raiz,8,b)
b, raiz = insAVL(raiz,12,b)
b, raiz = insAVL(raiz,14,b)
b, raiz = insAVL(raiz,15,b)
b, raiz = insAVL(raiz,16,b)
b, raiz = insAVL(raiz,17,b)
b, raiz = insAVL(raiz,2,b)
print("AVL")
print(pre_ordem(raiz,[]))

print()

raiz = insOrd(None,5)
raiz = insOrd(raiz,1)
raiz = insOrd(raiz,6)
raiz = insOrd(raiz,7)
raiz = insOrd(raiz,10)
raiz = insOrd(raiz,8)
raiz = insOrd(raiz,12)
raiz = insOrd(raiz,14)
raiz = insOrd(raiz,15)
raiz = insOrd(raiz,16)
raiz = insOrd(raiz,17)
raiz = insOrd(raiz,2)
print("Standard")
print(pre_ordem(raiz,[]))

