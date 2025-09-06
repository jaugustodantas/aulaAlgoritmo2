# Exercício 07
# Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
import math
numeros = []
def operacoes(*args):
    soma = sum(args)
    mult = math.prod(args)
    return f'o valor da soma do vetor é: {soma} e a multiplcacao é {mult}'

for x in range(5):
    numeros.append(int(input("Digite um número: ")))

print(operacoes(*numeros))