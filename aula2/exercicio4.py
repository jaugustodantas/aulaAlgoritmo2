import math
def calculoImc (peso,altura):
    return f'seu IMC = {(peso/(math.pow(altura,2))):.2f}'


altura = float(input("Digite a sua altura: "))
peso = float(input("digite seu peso: "))

print(calculoImc(peso,altura))