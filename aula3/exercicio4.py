# Exercício 04
# Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

letras = []
vogais =['a','e','i','o','u']
contadorConsoante = 0
for x in range(10):
    letras.append(input("Digite uma letra: "))

for l in letras:
    if l not in vogais:
        contadorConsoante +=1
        print(l)

print(f'foram contadas {contadorConsoante}')