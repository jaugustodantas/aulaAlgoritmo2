# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

arrayAge = []
arrayHeight = []
accumulator = 0
for x in range(30):
    arrayAge.append(int(input("Digite a idade do aluno: ")))
    arrayHeight.append(float(input("Digite a altura do aluno: ")))


arraySize = len(arrayHeight)

for h in arrayHeight:
    accumulator += h 
    heightAvg = accumulator/arraySize

for x in range(arraySize):
    if arrayAge[x] > 13 and arrayHeight[x]<heightAvg:
        counter +=1

print(counter)
