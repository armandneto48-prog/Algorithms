class Celula:
# construtor
    def __init__(self, valor=None, prox=None):
        self.valor = valor
        self.prox = prox
    
# inserir novo elemento no inicio
    def inserir_ini(inicio, novo):
        novo.prox = inicio
        return(novo)

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


class Celula2:
# construtor
    def __init__(self, valor=None, prox=None, ant=None):
        self.valor = valor
        self.prox = prox
        self.ant = ant

# inserir ordenado LDLigada
def insOrd2(inicio, val):
    novo = Celula2(val)
    
    if inicio is None:
        return novo
    atual=inicio
    pt= atual.prox
    ant= atual.ant
    
    while novo.valor>atual.valor:
        atual=inicio.prox
        pt=atual.prox
        ant=atual.ant
    if novo.prox is None:
        pt.prox=novo
    else:
        temp=ant
        temp1=atual
        atual=novo
        ant = temp.ant
        pt= temp1
        
    
        
        
    

# main prog
eu = Celula(1.0)
tu = Celula(3.2)
inicio = eu
inicio= Celula.inserir_ini(inicio, tu)
inicio= Celula.inserir_fim(inicio, Celula(5.5))
    

atual = inicio
while atual is not None:
    print(atual.valor)
    atual = atual.prox
    
    

    