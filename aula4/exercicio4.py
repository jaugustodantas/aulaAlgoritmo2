# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

nome = input("Digite seu nome: ")

for x in range (len(nome)+1):
    print(nome[:x])