while True:
    numero1 = int(input("Digite um número inteiro ou 0 para finalizar: "))
    numero2 = int(input("Digite um número inteiro ou 0 para finalizar: "))

    if numero1 == 0 or numero2 == 0 :
        break

    print(f'{numero1} + {numero2} = {numero1+numero2}')