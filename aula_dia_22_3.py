def pega(inicio, fim):
    while(inicio != None):
        pega = inicio
        inicio = fim
        fim = pega
    return pega

pega(5,10)

