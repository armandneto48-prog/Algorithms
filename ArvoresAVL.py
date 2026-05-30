#Construção de nós da árvore

class NoAVL:
	 # construtor
	def __init__(self, valor=None, bal = 0, esq=None, dir=None):
		self.valor = valor
		self.esq = esq
		self.dir = dir
		self.bal = bal # deve ser 1, 0, ou -1 para balanceado!
        
#Rotação para a direita

def RotateRight(A):
	B = A.esq   
	A.esq = B.dir
	B.dir = A  #B.dir é o subramo direito do ramo esquerdo de A (por causa da 1ªalínea)
	return B

#Rotação para a esquerda

def RotateLeft(B):
	A = B.dir
	B.dir = A.esq
	A.esq = B
	return A

#
def fixRight(A):
    B = A.dir #B é ramo direito da árvore A
    if(B.bal == -1):   # Se B desequilibrada para a direita
        A.bal = B.bal = 0 #zera-se o balanceamento (equilibra-se)
        A = RotateLeft(A) #Rotação de A para a esquerda (visto que inicialmente estava a pesar mais para a direita)
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
        return True, NoAVL(vals,0) #se não há raiz, cria uma com a classe NoAVL
    else:
        if(raiz.valor > vals): #mete o vals que queremos inserir no ramo esquerdo se for inferior ao valor da raiz (para manter a ordem)
            cresce, raiz.esq = insAVL(raiz.esq, vals, cresce)
            if(cresce):
                match raiz.bal: 
                    case 1: #LEFT Raiz estava desequilibrada para a esquerda e colocamos mais um elemento. Daí se fazer o fixLeft
                        raiz = fixLeft(raiz)
                        cresce = False
                    case 0: #Raiz estava balanceada mas colocamos um elemento à esq. Passou a ter desequilíbrio LEFT
                        raiz.bal = 1 # LEFT
                    case -1: #RIGHT Raiz estava desequilibrada para a direita e colocamos mais um elemento à esquera.Bal passa a zero - equilibrado
                        raiz.bal = 0 # BAL
                        cresce = False
        else:
            cresce, raiz.dir = insAVL(raiz.dir, vals, cresce) #mete o vals no lado direito (para manter a ordem)
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
print("Árvore construída com função insAVL, tem em conta o BALANCEAMENTO: \n Pré-ordem. \n")

print(pre_ordem(raiz,[]),"\n")

print("\n in_ordem: \n")
print(in_ordem(raiz,[]), "\n")

#6. Escreva uma função que dado uma árvore binária calcula a altura dessa árvore. Outra função que imprima os nós de um dado nível da árvore dada.

def calcAltura(raiz):
    if raiz is None:
        return 0
    alturaDta = calcAltura(raiz.dir)
    alturaEsq= calcAltura(raiz.esq)
    if alturaDta > alturaEsq:
        altura= alturaDta +1
    else:
        altura= alturaEsq +1
    return altura
    # return 1+(alturaDta if alturaDta > alturaEsq else alturaEsq)

altura=calcAltura(raiz)
    

print("Altura da árvore: ", altura)


nivel=2
def printaNos(raiz, nivel):
    if raiz is None:
        return []
    if nivel == 1:
        return raiz.valor
    subarvoreDta= printaNos(raiz.dir,nivel-1)
    subarvoreEsq= printaNos(raiz.esq,nivel-1)
    return (subarvoreEsq, subarvoreDta)
    
print("NÓS: \n",printaNos(raiz,nivel))
        
    
    
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
print("Standard, lista ordenada \n")
print("Pré-ordem: ", pre_ordem(raiz,[]))

print("\n in_ordem: \n")
print(in_ordem(raiz,[]))

def calcAlturaStandard(raiz):
    if raiz is None:
        return 0
    alturaDta = calcAlturaStandard(raiz.dir)
    alturaEsq= calcAlturaStandard(raiz.esq)
    if alturaDta > alturaEsq:
        altura= alturaDta +1
    else:
        altura= alturaEsq +1
    return altura

altura1=calcAlturaStandard(raiz)
print("Altura da árvore Standard:", altura1)