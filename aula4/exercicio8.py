# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa.
# Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

frase = input("Digite uma palavra ou frase: ")
fraseTratada = ''
fraseReversa = ''
for letra in frase:
    if letra.isalpha():
        fraseTratada += letra.lower()

for letra in reversed(fraseTratada):
    fraseReversa +=letra

if fraseReversa == fraseTratada:
    print ("Palídromo")
else:
    print (" não é Palídromo")