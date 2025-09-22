# Questão 3: Análise de Notas de Alunos (1.5 pontos)
# Crie um programa que ajude a analisar as notas de uma pequena turma. O programa deve:
# 1. Pedir ao usuário para digitar as notas de 5 alunos, uma por uma (notas de 0 a 10).
# 2. Armazenar essas notas em uma lista.
# 3. Após coletar todas as notas, calcular e imprimir a média da turma.
# 4. Contar e imprimir quantos alunos tiveram nota acima ou igual à média.

# Exemplo de interação:
# Digite a nota do aluno 1: 7.5
# Digite a nota do aluno 2: 8.0
# Digite a nota do aluno 3: 6.0
# Digite a nota do aluno 4: 9.0
# Digite a nota do aluno 5: 7.0
# Notas registradas: [7.5, 8.0, 6.0, 9.0, 7.0]
# Média da turma: 7.5
# Número de alunos acima ou igual à média: 3

notasAlunos = []
contador = 0
for x in range(5):
    notasAlunos.append(float(input(f"Digite a note do aluno{x+1}: ")))

print(f'Notas resgistradas {notasAlunos}')

media = sum(notasAlunos)/len(notasAlunos) #media da turma

print (f'A média da turma é {media}')
for nota in notasAlunos:
    if nota >= media:
        contador+=1

print(f'Número de alunos acima ou igual a média: {contador}')