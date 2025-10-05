# Jogo de Craps.
# Faça um programa que implemente um jogo de Craps.
# O jogador lança um par de dados, obtendo um valor entre 2 e 12.
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

def jogar_dados():
    return random.randint(1, 6) + random.randint(1, 6)

print("Bem-vindo ao jogo de Craps!")
primeira = jogar_dados()
print(f"Você tirou {primeira}")
if primeira in [7, 11]:
    print("Natural! Você ganhou!")
elif primeira in [2, 3, 12]:
    print("Craps! Você perdeu!")
else:
    ponto = primeira
    print(f"Seu ponto é {ponto}. Continue jogando...")
    while True:
        nova = jogar_dados()
        print(f"Você tirou {nova}")
        if nova == ponto:
            print("Você tirou o ponto novamente! Você ganhou!")
            break
        elif nova == 7:
            print("Você tirou 7 antes do ponto! Você perdeu!")
            break
