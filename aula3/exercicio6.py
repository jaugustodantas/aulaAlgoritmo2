# Exercício 06
# Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
notaAluno = []
mediaAlunos = []

def media (*args):
     media = sum(args) /4
     mediaAlunos.append(media)    


for y in range (10):
    for x in range(4):
        notaAluno.append(float(input("Digite uma nota: ")))

    media(*notaAluno)



for m in mediaAlunos:
    if m >= 7.0:
        print(m)
