class Stack:  # stack de inteiros usando um array

    # construtor
    def __init__(self, size=1):
        self.stack = []
        self.size = size
        for i in range(1,size):
            self.stack += [0]
        self.idx = 0

    def empty(self):
        return self.idx == 0

    def pop(self):
        if( not self.empty()):
            self.idx -= 1
            tmp = self.stack[self.idx]
            return tmp
        else:
            return None

    def push(self, x):
        if(self.idx < self.size):
            self.stack[self.idx] = x
            self.idx += 1

    def peek(self):
        if(not self.empty()):
            return self.stack[self.idx-1]


# main
'''s = Stack(10)
s.push(1)
s.push(2)
print(s.peek())
s.push(3)
print(s.peek())
s.pop()
print(s.peek())
print(s.empty())
s.pop()
print(s.peek())
s.push(3)
s.push('+')
s.push(5)
s.push(2)
s.push('/')
print()
print()
while(not s.empty()):
        print(s.pop())'''
        
        
#Implementar uma calculadora pós-fixo que usa uma stack para calcular as 
#operações aritméticas básicas. Por exemplo para a expressão pós-fixa     
#5 6 12 4 / + *      
#dá como resultado  o  valor 45.



def calcula(a):
    f = Stack(10)
    for x in a.split():
        if x.isdigit():
            f.push(float(x))
        else:
            e1 = f.pop()
            e2 = f.pop()
            operador=x
            resultado = 0.0
            match operador:
                case '+':
                    resultado = e1+e2
                case '-':
                    resultado= e1-e2
                case '*':
                    resultado = e1*e2
                case '/':
                    resultado = e1/e2
            f.push(resultado)

    return f.peek()

#main            
print(calcula("2 3 + 5 /"))

'''4. Implemente um avaliador de expressões algébricas em termos de 
parênteses usados. Considere todos os parênteses possíveis – ‘{}’, ‘()’, ‘[]’. 
O programa deve indicar se uma expressão está bem balanceada em 
termos de parênteses e se não for válida indicar o erro (excesso ou falta 
de parêntese ou mal emparelhados) e.g.,   (a + { c -d} * a –[{x-y}/2]    tem 
falta de um ‘)’. Hint: use uma stack de parênteses…'''
                                           
def avaliador(b):
    g=Stack(10)
    for e in b.split():
        if e.isdigit():
            return 
        else:
            g.push(e)
            print(g.peek())
            
    #criar dicionário em que associo um parentesis direito ao esquerdo e depois verificar se coincidem
            

avaliador("4+3-(5*8)+(1")
            
        
            
        

    
    


 