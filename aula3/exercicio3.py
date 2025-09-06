# Exercício 03
# Faça um programa que leia 4 notas, mostre as notas e a média na tela.

notas=[]
nota =0

for x in range(4):
    notas.append(float(input("Digite uma nota: ")))

for x in range(4):
    nota += notas[0]
    
print(f'{notas} e média = {nota/4}')