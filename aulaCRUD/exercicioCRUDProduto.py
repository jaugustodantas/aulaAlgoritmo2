import os
listaDeProdutos = []

def limpaTela():
    os.system('cls' if os.name =='nt' else 'clear')


def cadastraProduto ():
    produto = {
        "ID": int(input("digite o id do produto: ")),
        "Nome": input("digite o nome do produto: "),
        "Preco": float(input("Digite o preço do produto: "))
    }
    return produto

def listaProduto ():
    for p in listaDeProdutos:
        for chave, valor in p.items():
            print(chave,valor)

def atualizaProduto (id):
    for p in listaDeProdutos:
        if p["ID"] == int(id):
            p["Preco"] = float(input("Digite o novo preço do produto"))

def deletaProduto(id):
    for p in listaDeProdutos:
        if p["ID"] == int(id):
            listaDeProdutos.remove(p)


while True:
    
    opcao = input("Digite 1 para sair \n" \
                    "Digite 2 para cadastrar os produtos \n"
                    "Digite 3 para listar os protudos \n"
                    "Digite 4 para atualizar um produto \n"
                    "Digite 5 para deletar um produto \n")
    
    if opcao =="1":
        limpaTela()
        break
    elif opcao =="2":
        listaDeProdutos.append(cadastraProduto())
    elif opcao =="3":
        listaProduto()
    elif opcao =="4":
        atualizaProduto(int(input("Digite o ID que deja atualizar: ")))
    else:
        deletaProduto(int(input("Digite o ID que deja excluir: ")))