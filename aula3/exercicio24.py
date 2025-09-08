# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
from collections import Counter
import random

dices = []

for x in range (100):
    dices.append(random.randint(1,6))


totalRolls = Counter(dices)

for n, ocourrence in totalRolls.items():
    print(f'O número {n} saiu {ocourrence} vezes')