class Celula:
	 # construtor
	def __init__(self, valor=None, prox=None):
		self.valor = valor
		self.prox = prox
        
# inserir novo elemento no inicio
def inserir_ini(inicio, novo):
	novo.prox = inicio
	return(novo)

'''# main prog
eu = Celula(1.0)
tu = Celula(3.2)
inicio = None
inicio = inserir_ini(inicio,eu)
inicio = inserir_ini(inicio,tu)'''

# inserir no fim
def inserir_fim(inicio,novo):
	if(inicio is None):
		return novo
	pt = inicio
	while(pt.prox is not None):
		pt = pt.prox
	pt.prox = novo
	novo.prox = None
	return inicio


# main prog
eu = Celula(1.0)
tu = Celula(3.2)
inicio = eu
inicio = inserir_ini(inicio, tu)
inicio = inserir_fim(inicio, Celula(5.5))


#1.  Considere a definição de lista (dupla e simplesmente) ligada: 
#a. Escreva uma função que dado o inicio de uma lista simplesmente ligada inverte essa lista, retornando o novo inicio.

def printa(inicio):
    pt=inicio
    while(pt is not None):
        print(pt.valor)
        pt=pt.prox
        
print(printa(inicio))

def inverter(inicio):
    anterior=None
    atual=inicio
    pt=inicio.prox
    while(pt.prox is not None):
        anterior=atual
        inicio = pt.prox
    while(anterior is not None):
       
        
print(inverter(inicio))
    