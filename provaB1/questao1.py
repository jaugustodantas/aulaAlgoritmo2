# Questão 1: Verificador de Palíndromo (1.0 ponto)
# Crie um programa Python que solicite ao usuário uma palavra ou frase. O programa deve
# verificar se a palavra/frase é um palíndromo, ignorando espaços e considerando letras
# maiúsculas e minúsculas como iguais. Um palíndromo é uma sequência que se lê da
# mesma forma de trás para frente (ex: "ovo", "arara", "A base do teto desaba").
# Dicas:
# ● Converta a string para minúsculas.
# ● Remova os espaços.
# ● Compare a string original (tratada) com sua versão invertida.
# Exemplo de interação:
# Digite uma palavra ou frase: arara
# 'arara' é um palíndromo.
# Digite uma palavra ou frase: ola
# 'ola' NÃO é um palíndromo.
# Digite uma palavra ou frase: Apos a Sopa
# 'Apos a Sopa' é um palíndromo.
stringBruta =""
stringTratada = ""
frase = input("Digite uma frase: ")

for x in frase:
    if x.isalpha():
        stringBruta += x.lower()

for x in reversed(stringBruta):
    stringTratada += x

if stringBruta == stringTratada:
    print(f'a fase {frase} é um palídromo')
else:
    print(f'a frase {frase} não é um palídromo')