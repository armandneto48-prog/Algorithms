
num = 0

N = [1,2,3,4,5,6]

def printa_mult3(N):

    # Imprime o cabeçalho concatenando o texto com o número N convertido em string
    print("multiplos de 3 entre 1 e " + str(N)) 
    
    # O ciclo for percorre todos os números de 1 até N (inclusive)
    for num in range(1, N + 1): 
        
        # Se o resto da divisão do número por 3 for estritamente igual a 0
        if (num % 3 == 0): 
            print(num)  # O número é impresso apenas se passar na condição acima




