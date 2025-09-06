# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".
questions = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]
verdict = {
    "Inocente":[0,1],
    "Suspeito":[2],
    "Cumplice":[3,4],
    "Assassino":[5]
}

anwsers = []
print("digite s/n para as perguntas a baixo:")
for q in questions:
    print(f'{q}')
    anwsers.append(input().strip().lower())

total = anwsers.count('s')
for key,value in verdict.items():
    if total in value:
        print(key)