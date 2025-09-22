# Questão 5: Analisador Simples de Palavras (1.5 pontos)
# Crie um programa Python que solicite ao usuário que digite uma palavra ou frase. O
# programa deve então realizar as seguintes operações com a string fornecida e imprimir os
# resultados:
# 1. Imprimir a palavra/frase em letras maiúsculas.
# 2. Contar e imprimir quantas vezes a letra 'a' (minúscula ou maiúscula) aparece na
# palavra/frase.
# 3. Substituir todos os espaços em branco por hífens (-) e imprimir a nova frase.
# 4. Imprimir os primeiros 3 caracteres da palavra/frase.
# Exemplo de interação:
# Digite uma palavra ou frase: Algoritmos e Programacao em Python
# Maiúsculas: ALGORITMOS E PROGRAMACAO EM PYTHON
# A letra 'a' aparece: 3 vezes
# Com hífens: Algoritmos-e-Programacao-em-Python
# Primeiros 3 caracteres: Alg



texto = input("Digite uma palavra ou frase: ")
print("Maiúsculas:", texto.upper())
quantidade= texto.count('a')
print(f"A letra 'a' aparece: {quantidade} vezes")
textoHifen = texto.replace(" ", "-")
print("Com hífens:", textoHifen)
print("Primeiros 3 caracteres:", texto[:3])

