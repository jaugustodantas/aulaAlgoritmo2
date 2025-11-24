listaLanches = []
while True:
    nomeLanche = input("Digite o nome do lanche: ")
    precoLanche = input("Digite o preço do lanche: ")

    lanche = {'nome': nomeLanche, 'preco': precoLanche}
    listaLanches.append(lanche)

    opcao = input("Deseja cadastrar outro aluno? (s/n): ").lower()
    if opcao == 'n':
        break

arquivo = open("cadastroLanches.txt", "a")

for lanche in listaLanches:
    arquivo.write(f"Nome: {lanche['nome']}, Preço: {lanche['preco']}\n")