# Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere P, se seu argumento for positivo, e N, se seu argumento for zero ou negativo.

def testNumber (num):
    if num > 0:
        return f'O número {num} é possitivo'
    else:  
        return f'O número {num} é negativo'
    

number = int(input("Digite um número: "))

print(testNumber(number))