# Questão 2: Gerenciador Simples de Contatos (1.5 pontos)
# Desenvolva um programa que permita ao usuário gerenciar uma pequena lista de contatos.
# O programa deve:
# 1. Começar com uma lista vazia de contatos.
# 2. Permitir que o usuário adicione o nome de 3 contatos à lista, um por um, utilizando
# um loop.
# 3. Após adicionar, o programa deve imprimir a lista de contatos numerada (ex: "1. João
# Silva").
# 4. Em seguida, pergunte ao usuário o nome de um contato para buscar.
# 5. Se o contato for encontrado na lista, imprima: "Contato '[Nome do Contato]'
# encontrado na posição [índice + 1] da lista.".
# 6. Se o contato não for encontrado, imprima: "Contato '[Nome do Contato]' não
# encontrado.".
# Exemplo de interação:
# Digite 3 nomes de contatos para sua lista.
# Contato 1: Alice
# Contato 2: Bruno
# Contato 3: Carla
# Seus contatos:
# 1. Alice
# 2. Bruno
# 3. Carla
# Qual contato você deseja buscar? Bruno
# Contato 'Bruno' encontrado na posição 2 da lista.
# Qual contato você deseja buscar? Daniel
# Contato 'Daniel' não encontrado.

listaContato = []
contador = 1
quantidadeRegistro = int(input('Digite quantos contatos quer cadastrar: '))

for x in range(quantidadeRegistro):  #faz o loop para registrar o número de contatos que o usuário deseja cadastrar
    listaContato.append(input(f"Contato {contador}: ")) #insere o contato a lista
    contador +=1

print("Seus contatos: ")
contador =1 
for c in listaContato:
    print(f'{contador}.\t {c}')
    contador +=1

contato= input("Qual contato deseja buscar? ")
if contato in listaContato:
    print(f'Contato {contato} na posição {listaContato.index(contato)+1}')
else:
    print(f'Contato {contato} não encontrado')