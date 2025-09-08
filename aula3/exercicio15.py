# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;
arrayGrades = []
while True:
    grade = float(input("Digite uma nota: "))
    if grade == -1:
        break

    arrayGrades.append(grade)

print(f'A quantidade de notas foram {len(arrayGrades)}')
print(f'A soma das notas é {sum(arrayGrades)}')
gradesAvg = sum(arrayGrades)/len(arrayGrades)
print(f'A media das notas é {gradesAvg:.2f}')
print(arrayGrades)
for g in reversed(arrayGrades):
    print(g)

print("fim")