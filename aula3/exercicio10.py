# Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos 
# elementos intercalados dos dois outros vetores.

v1 = []
v2= []
v3 = []

def preencherVetor (vetor):
    print("digite o valor para um vetor")
    for x in range(10):
        vetor.append(input("Digite o valor de entrada: "))


preencherVetor(v1)
preencherVetor(v2)
for x in range(10):
    v3.append(v1[x])
    v3.append(v2[x])

print(v3)