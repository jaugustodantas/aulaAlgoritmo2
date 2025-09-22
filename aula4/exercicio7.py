# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

caracteresParaSeremContados = [' ','a','e','i','o','u']
novaFrase = ''
frase = input("Digite uma frase: ")
for letra in frase:
    novaFrase += letra.lower()

tst = set(novaFrase)
for x in tst:
    if x in caracteresParaSeremContados:
        valor =novaFrase.count(x)
        if x == ' ':
            print(f'Existe(m) {valor}  espaço')
            continue
        print(f'Existe(m) {valor} {x}')