# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador poderá errar 6 vezes antes de ser enforcado.

# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!

# Digite uma letra: O
# A palavra é: _ _ _ _ O

# Digite uma letra: E
# A palavra é: _ E _ _ O

# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

import random

def impressao(palavra,letras):
    return f'A palavra é: {' '.join([letra if letra in letras else '_' for letra in palavra])}'


contador = 0
listaPalavras=[]
lestrasDescobertas = []
with open('listaPalavras.txt','r',encoding='utf-8') as o:
    linhas = o.readlines()
    for linha in linhas:
        listaPalavras.append(linha.strip().upper())

palavra = random.choice(listaPalavras)
print(impressao(palavra,lestrasDescobertas))
while True:
    l = input("Digite uma letra: ").upper()
    if l in lestrasDescobertas:
        print(f'Você já tentou a letra {l}')
        continue

    lestrasDescobertas.append(l)
    if l in palavra:
        print(impressao(palavra,lestrasDescobertas))
    else:
        contador +=1
        print(f'Você errou pela {contador}º vez. Tente denovo')
        if contador == 6:
            break

    if all(letra in lestrasDescobertas for letra in palavra):
        print(f'Parabéns você descobriu a palavra {impressao(palavra,lestrasDescobertas)}')
        break
