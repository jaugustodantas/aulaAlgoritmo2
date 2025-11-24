import os

listaDeUsuarios = []
listadeMusicas = []

# Utilitários
def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Usuário
def cadastroUsuario():
    limpaTela()
    idUsuario = len(listaDeUsuarios) + 1
    nome = input("Digite o nome do usuário: ")
    sobreNome = input("Sobrenome do usuário: ")

    usuario = {
        "id": idUsuario,
        "nome": nome,
        "sobreNome": sobreNome,
        "musicasFavoritas": []
    }

    adicionar_musicas_favoritas(usuario)
    listaDeUsuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    input("\nPressione Enter para continuar...")

def listarUsuario():
    limpaTela()
    for u in listaDeUsuarios:
        print(f"ID: {u['id']}")
        print(f"Nome: {u['nome']} {u['sobreNome']}")
        print("Músicas favoritas:")
        for id_musica in u["musicasFavoritas"]:
            musica = next((m for m in listadeMusicas if m["id"] == id_musica), None)
            if musica:
                print(f"  - {musica['nomeDaMusica']} ({musica['artista']})")
            else:
                print(f"  - [ID {id_musica} - não encontrada]")
        print("-" * 40)
    input("\nPressione Enter para continuar...")

def deletarUsuario():
    limpaTela()
    try:
        id_del = int(input("Digite o ID do usuário a ser deletado: "))
        for u in listaDeUsuarios:
            if u["id"] == id_del:
                listaDeUsuarios.remove(u)
                print("Usuário removido com sucesso.")
                break
        else:
            print("Usuário não encontrado.")
    except ValueError:
        print("Entrada inválida.")
    input("\nPressione Enter para continuar...")

def alterarUsuario():
    limpaTela()
    try:
        id_alterar = int(input("Digite o ID do usuário a ser alterado: "))
        for u in listaDeUsuarios:
            if u["id"] == id_alterar:
                u["nome"] = input("Novo nome: ")
                u["sobreNome"] = input("Novo sobrenome: ")
                adicionar_musicas_favoritas(u)
                print("Usuário alterado com sucesso.")
                break
        else:
            print("Usuário não encontrado.")
    except ValueError:
        print("Entrada inválida.")
    input("\nPressione Enter para continuar...")

# Música
def cadastarMusica():
    limpaTela()
    idMusica = len(listadeMusicas) + 1
    musica = {
        "id": idMusica,
        "nomeDaMusica": input("Digite o nome da música: "),
        "artista": input("Qual o artista? "),
        "genero": input("Qual gênero da música? "),
        "album": input("Qual o álbum da música? ")
    }
    listadeMusicas.append(musica)
    print("Música cadastrada com sucesso!")
    input("\nPressione Enter para continuar...")

def lerMusicas():
    limpaTela()
    for m in listadeMusicas:
        for chave, valor in m.items():
            print(f'{chave}: {valor}')
        print("-" * 40)
    input("\nPressione Enter para continuar...")

def atualizarMusica():
    limpaTela()
    try:
        id_m = int(input("Digite o ID da música a ser atualizada: "))
        for m in listadeMusicas:
            if m["id"] == id_m:
                m["nomeDaMusica"] = input("Novo nome da música: ")
                m["artista"] = input("Novo artista: ")
                m["genero"] = input("Novo gênero: ")
                m["album"] = input("Novo álbum: ")
                print("Música atualizada com sucesso.")
                break
        else:
            print("Música não encontrada.")
    except ValueError:
        print("Entrada inválida.")
    input("\nPressione Enter para continuar...")

def deletarMusica():
    limpaTela()
    try:
        id_del = int(input("Digite o ID da música a ser deletada: "))
        for m in listadeMusicas:
            if m["id"] == id_del:
                listadeMusicas.remove(m)
                print("Música removida com sucesso.")
                break
        else:
            print("Música não encontrada.")
    except ValueError:
        print("Entrada inválida.")
    input("\nPressione Enter para continuar...")

# Funções auxiliares
def listarTodasMusicas():
    print("\n--- Músicas Disponíveis ---")
    for m in listadeMusicas:
        print(f"{m['id']} - {m['nomeDaMusica']} ({m['artista']})")

def adicionar_musicas_favoritas(usuario):
    if not listadeMusicas:
        print("\nNenhuma música cadastrada ainda.")
        return
    listarTodasMusicas()
    try:
        ids = input("Digite os IDs das músicas favoritas separados por vírgula (ou deixe em branco): ")
        if ids.strip() == "":
            return
        ids_list = [int(i.strip()) for i in ids.split(",") if i.strip().isdigit()]
        usuario["musicasFavoritas"] = []
        for id_musica in ids_list:
            if any(m["id"] == id_musica for m in listadeMusicas):
                usuario["musicasFavoritas"].append(id_musica)
            else:
                print(f"ID {id_musica} não encontrado.")
    except ValueError:
        print("Erro ao processar os IDs.")

# Exportar dados
def exportar_usuarios_para_txt(listaDeUsuarios, listadeMusicas, caminho="usuarios.txt"):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for usuario in listaDeUsuarios:
            arquivo.write(f"ID: {usuario['id']}\n")
            arquivo.write(f"Nome: {usuario['nome']} {usuario['sobreNome']}\n")
            arquivo.write("Músicas Favoritas:\n")
            for id_musica in usuario["musicasFavoritas"]:
                musica = next((m for m in listadeMusicas if m["id"] == id_musica), None)
                if musica:
                    arquivo.write(f"  - {musica['nomeDaMusica']} ({musica['artista']})\n")
                else:
                    arquivo.write(f"  - [ID {id_musica} - não encontrada]\n")
            arquivo.write("-" * 40 + "\n")
    print("\nArquivo 'usuarios.txt' gerado com sucesso.")

# Menus
def exibir_menu_principal():
    limpaTela()
    print("=" * 50)
    print(f"{'MENU PRINCIPAL':^50}")
    print("=" * 50)
    print(f"{'[1] Menu Usuários':<25}{'[2] Menu Músicas':>25}")
    print("-" * 50)
    print(f"{'[S] Sair':^50}")
    print("=" * 50)

def exibir_menu_usuarios():
    limpaTela()
    print("=" * 50)
    print(f"{'MENU USUÁRIOS':^50}")
    print("=" * 50)
    print(f"{'[I] Inserir usuário':<25}{'[A] Alterar usuário':>25}")
    print(f"{'[L] Listar usuários':<25}{'[E] Excluir usuário':>25}")
    print("-" * 50)
    print(f"{'[V] Voltar ao menu principal':^50}")
    print("=" * 50)

def exibir_menu_musicas():
    limpaTela()
    print("=" * 50)
    print(f"{'MENU MÚSICAS':^50}")
    print("=" * 50)
    print(f"{'[I] Inserir música':<25}{'[A] Alterar música':>25}")
    print(f"{'[L] Listar músicas':<25}{'[E] Excluir música':>25}")
    print("-" * 50)
    print(f"{'[V] Voltar ao menu principal':^50}")
    print("=" * 50)

def crud_usuarios():
    while True:
        exibir_menu_usuarios()
        opcao = input("Escolha uma opção: ").upper()
        if opcao == "I":
            cadastroUsuario()
        elif opcao == "A":
            alterarUsuario()
        elif opcao == "L":
            listarUsuario()
        elif opcao == "E":
            deletarUsuario()
        elif opcao == "V":
            break
        else:
            print("Opção inválida.")
            input("\nPressione Enter para continuar...")

def crud_musicas():
    while True:
        exibir_menu_musicas()
        opcao = input("Escolha uma opção: ").upper()
        if opcao == "I":
            cadastarMusica()
        elif opcao == "A":
            atualizarMusica()
        elif opcao == "L":
            lerMusicas()
        elif opcao == "E":
            deletarMusica()
        elif opcao == "V":
            break
        else:
            print("Opção inválida.")
            input("\nPressione Enter para continuar...")

# Programa principal
while True:
    exibir_menu_principal()
    opcao = input("Escolha uma opção: ").upper()

    if opcao == "1":
        crud_usuarios()
    elif opcao == "2":
        crud_musicas()
    elif opcao == "S":
        exportar_usuarios_para_txt(listaDeUsuarios, listadeMusicas)
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para continuar...")




