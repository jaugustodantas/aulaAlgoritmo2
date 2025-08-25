

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
teste = input("Digite s se você gosta de programar ou n caso não goste: ").strip().lower()
if teste == 's':
    teste = True
    sl = "gosta"
else:
    teste = False
    sl= "não gosta"

print(f'seu nome é {nome} a varável nome é do tipo {type(nome)}')
print(f'sua idade é {idade} anos a varável idade é do tipo {type(idade)}')
print(f'Você {sl} de programar teste é do tipo {type(teste)}')