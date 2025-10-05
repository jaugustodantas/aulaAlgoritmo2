# Embaralha palavra.
# Construa uma função que receba uma string como parâmetro e devolva outra string com os caracteres embaralhados.
# Por exemplo: se a função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
# Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

import random

def embaralhar_palavra(palavra):
    palavra = palavra.lower()
    # converte a string em lista para poder embaralhar
    letras = list(palavra)
    random.shuffle(letras)
    palavra_embaralhada = ''.join(letras)
    return palavra_embaralhada

# Exemplo de uso:
print(embaralhar_palavra("Python"))

