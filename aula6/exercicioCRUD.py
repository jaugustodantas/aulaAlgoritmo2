import os
lista_jogadores = []

def limpar_tela():
    # 'cls' limpa o terminal no Windows
    # 'clear' limpa o terminal no Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')


def  inserirJogador ():
    nome = input("Digite o nome: ")
    posicao = input("Digite a posição: ")
    numero_uniforme = int(input("Digite o número do uniforme:"))

    jogador ={"nome":nome, 
            "posicao":posicao, 
            "numero_uniforme": numero_uniforme
               }

    lista_jogadores.append(jogador)


def listarJogadores():
    for item in lista_jogadores: #itera a lista
        for chave,valor in item.items(): #itera o dicionário para imprimir chave e valor
            print(chave,valor)



def editarJogador ():
    nome_alterar = input("Digite o nome do jogador: ")
    for item in lista_jogadores:
         if item['nome']== nome_alterar:
             item['nome']=input("Digite o novo nome: ")
         else:
             print("Não encontrei o jogador!")


def excluirJogador ():
    excluir_jogador = input("Digite o nome do jogador: ")
    for jogador in lista_jogadores:
        if jogador['nome'] == excluir_jogador:
            lista_jogadores.remove(jogador)


def exibir_menu():
    print("=" * 50)
    print(f"{'MENU PRINCIPAL':^50}")
    print("=" * 50)
    print(f"{'[I] Inserir jogador':<25}{'[A] Alterar jogador':>25}")
    print(f"{'[L] Listar jogador':<25}{'[E] Excluir jogador':>25}")
    print("-" * 50)
    print(f"{'[S] Sair':^50}")
    print("=" * 50)

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip().upper()
    if opcao == 'S':
        limpar_tela()
        break
    elif opcao == 'I':
        inserirJogador()
        limpar_tela()   
    elif opcao == 'L':
        listarJogadores()
    elif opcao == 'A':
        editarJogador()
    elif opcao == 'E':
        excluirJogador()
    else:
        print("Opção invállida")

    

