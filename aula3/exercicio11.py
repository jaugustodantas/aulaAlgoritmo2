# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

v1 = []
v2= []
v3 = []
v4=[]
def preencherVetor (vetor):
    print("digite o valor para um vetor")
    for x in range(10):
        vetor.append(input("Digite o valor de entrada: "))


preencherVetor(v1)
preencherVetor(v2)
preencherVetor(v3)
for x in range(10):
    v4.append(v1[x])
    v4.append(v2[x])

print(v4)