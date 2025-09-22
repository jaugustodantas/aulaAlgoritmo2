# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

string1 = input("Digite uma frase: ")
string2 = input("Digite uma frase: ")
tamanhoString1 = len(string1)
tamanhoString2 = len(string2)

print(f'Tamanho de \"{string1}\": {tamanhoString1} caracteres')
print(f'Tamanho de \"{string2}\": {tamanhoString2} caracteres')

if tamanhoString1 == tamanhoString2:
    print("As duas strings são de tamanhos diferentes")
else:
    print("As duas strings são de tamanhos iguais")

if string1 == string2:
    print("As duas strings possuem conteúdo iguais.")
else:
    print("As duas strings possuem conteúdo diferentes.")