# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
nome = input("Digite o seu nome: ")
tst = len(nome)
for x in range(tst,0,-1):
    print(nome[:x])