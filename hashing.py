# 6)

V=[1,3,7,4,5,1,3,1,3,9,10,6,22,1,5,7]

#Verificar se são todos distintos
#Quantos diferentes tem?

#c É DICIONÁRIO, TABELA DE HASH!
def conta(V):
    N=len(V)
    c= {}
    for k in V:
        if k not in c:
            c[k]=1
        else:
            c[k]+=1
    return len(c)

numDiferentes= conta(V)
print('Há ', numDiferentes, ' números diferentes')

#7) Hash pode ter palavras 

tex= "era era era era uma noite triste e fria"
 
d={}

def contaPalavras(tex,d):
    for a in tex.split():
        if a not in d:
            d[a]=1
        else:
            d[a]+=1
    return len(d)

print('Há ', contaPalavras(tex), 'palavras distintas')

print(d['era'])


        