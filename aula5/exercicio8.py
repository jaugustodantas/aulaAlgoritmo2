# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.


#Nota esse algoritmo entende que o usuário vai entrar os numeros de 0 a 9 sem o zero a esquerda
#Ex 5 é correto 05 não vai entrar
def digitos(numero):
    numeroC = str(numero)
    return f' O numero {numero} possui {len(numeroC)} digitos'


num = int(input("Digite um número inteiro: "))
print(digitos(num))