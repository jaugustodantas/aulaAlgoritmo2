# Exercício 08
# Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

modelo = {
    "nome":None, 
    "idade":None,
    "altura": None
}
pessoas=[]

for x in range(5):
    novaPessoa = {}
    for chave in modelo:
        valor = input(f"digite {chave.capitalize()} da pessoa: ")
        novaPessoa[chave] = valor
    pessoas.append(novaPessoa)

for pessoa in reversed(pessoas):
    print(f"Nome: {pessoa['nome']}")
    print(f"idade: {pessoa['idade']}")
    print(f"altura: {pessoa['altura']}")