# Exercício 05
# Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
numerosPar = []
numerosImpar = []

for x in range (20):
    numeros.append(int(input("Digite un número")))

for n in numeros:
    if n%2==0:
        numerosPar.append(n)
    else:
        numerosImpar.append(n)