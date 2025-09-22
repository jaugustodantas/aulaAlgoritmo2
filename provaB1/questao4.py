# Questão 4: Gerenciador Básico de Tarefas (1.5 pontos)
# Crie um programa que gerencie uma lista de tarefas. O programa deve:
# 1. Iniciar com uma lista vazia de tarefas.
# 2. Permitir que o usuário adicione até 5 tarefas à lista, uma por uma, utilizando um
# loop.
# 3. Após adicionar as tarefas, o programa deve imprimir todas as tarefas numeradas
# (ex: "1. Comprar pão").
# 4. Em seguida, o programa deve perguntar ao usuário qual tarefa ele deseja remover
# (pelo número).
# 5. Após a remoção (se o número for válido), o programa deve imprimir a lista
# atualizada de tarefas.
# Exemplo de interação:
# Digite 5 tarefas para sua lista.
# Tarefa 1: Comprar pão
# Tarefa 2: Estudar Python
# Tarefa 3: Fazer exercício
# Tarefa 4: Ligar para Maria
# Tarefa 5: Preparar jantar
# Suas tarefas:
# 1. Comprar pão
# 2. Estudar Python
# 3. Fazer exercício
# 4. Ligar para Maria
# 5. Preparar jantar

# Qual tarefa você deseja remover (digite o número)? 3
# Lista de tarefas atualizada:
# 1. Comprar pão
# 2. Estudar Python
# 3. Ligar para Maria
# 4. Preparar jantar

# Observação: Não se preocupe com tratamento de erro para entradas inválidas (ex: usuário
# digitando texto ao invés de número para remover).

tarefas =[]
for x in range(5):
    tarefas.append(input(f'Tarefa {x+1}: '))

print("Suas tarefas")
for tarefa in tarefas:
    print(f'{tarefas.index(tarefa)+1}. {tarefa}')

numeroTarefaRemover = int(input("Qual tarefa você deseja remover (digite o número)? "))
tarefas.pop(numeroTarefaRemover-1)
print("Lista de tarefas atualizada:")
for tarefa in tarefas:
    print(f'{tarefas.index(tarefa)+1}. {tarefa}')