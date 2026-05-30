class Celula:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None 
    
def inserir_ini(inicio,novo):
    novo.prox = inicio
    return novo 


def imprimir(inicio):
    pt = inicio
    while pt is not None:
        print(pt.valor)
        pt = pt.prox
    

def pega(inicio, fim):
    while(inicio != None):
        pega = inicio
        inicio = fim
        fim = pega
    return pega



#prog principal
inicio = Celula(1.0)
inicio = inserir_ini(inicio,Celula(3.0))
inicio = inserir_ini(inicio,Celula(2.0))
imprimir(inicio)

