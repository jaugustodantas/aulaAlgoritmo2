# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
acumulador = 0
numeros=[]
for x in range (10):
    numeros.append(int(input("Digite um número: ")))

for n in numeros:
    quadrado = pow(n,2)
    acumulador = acumulador + quadrado

print(acumulador)