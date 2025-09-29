# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas.
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
import random

# Lê palavras do arquivo
listaPalavras = []
with open('listaPalavras.txt', 'r', encoding='utf-8') as o:
    linhas = o.readlines()
    for linha in linhas:
        listaPalavras.append(linha.strip().upper())

# Escolhe e embaralha
palavra = random.choice(listaPalavras)
letras = list(palavra)
random.shuffle(letras)
embaralhada = "".join(letras)

print("=== Jogo da Palavra Embaralhada ===")
print("Você tem 6 tentativas para adivinhar a palavra.")
print(f"A palavra é: {embaralhada}")

tentativas = 6
venceu = False

while tentativas > 0:
    chute = input("Digite sua resposta: ").strip().upper()
    
    if chute == palavra:
        venceu = True
        break
    else:
        tentativas -= 1
        print(f"Errado! Você ainda tem {tentativas} tentativa(s).")

if venceu:
    print(f"Parabéns! Você acertou: {palavra}")
else:
    print(f"Você perdeu! A palavra era: {palavra}")


