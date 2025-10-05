# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def fazReverso (numero):
    numReverso =""
    for d in reversed(numero):
        numReverso += d
    return f'{numero} -> {numReverso}'



numero = input("Digite um número: ")
print(fazReverso(numero))