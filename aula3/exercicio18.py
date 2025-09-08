# Observe que os votos inválidos e o zero final não devem ser computados como votos.
# O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays.
# O programa deverá executar o cálculo do percentual de cada jogador através de uma função.
# Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
# A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo.
# O disposição das informações deve ser o mais próxima possível ao exemplo.
# Os dados são fictícios e podem mudar a cada execução do programa.
# Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.

# Enquete: Quem foi o melhor jogador?

# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50
# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0

# Resultado da votação:

# Foram computados 8 votos.


# Jogador         Votos           %
# 9               4               50,0%
# 10              3               37,5%
# 11              1               12,5%
# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
from collections import Counter


votes = []

while True:
    playerNumber = int(input("Digite o número do jogador: "))
    if playerNumber  == 0:
        break
    if playerNumber > 23:
        print("Apenas números entre 1 e 23 são válidos")
        continue

    votes.append(playerNumber)

arrayLen = len(votes)
totalVotes = Counter(votes)

print(f'{'Jogador':<15}{'Votos':<15}{'%':<5}')
for number,occurence in totalVotes.items():
    print(f'{number:<15}{occurence:<15}{((occurence/arrayLen)*100):<5.1f}%')  #o < serve para dar o espaçamento no print
