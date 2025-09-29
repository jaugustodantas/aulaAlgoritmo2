# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx 
# e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
# Validação simples de CPF
# Usando apenas strings, laços e condições

cpf = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")

if len(cpf) != 14: 
    print("Inválido: tamanho incorreto")
else:
    if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
        print("Inválido: formato incorreto")
    else:
        numeros = ""
        for c in cpf:
            if c.isdigit():   
                numeros += c

        if len(numeros) != 11:
            print("Inválido: dígitos incorretos")
        elif numeros == numeros[0] * 11: 
            print("Inválido: todos dígitos iguais")
        else:
            soma = 0
            peso = 10
            for i in range(9):
                soma += int(numeros[i]) * peso
                peso -= 1
            resto = soma % 11
            dv1 = 0 if resto < 2 else 11 - resto

            soma = 0
            peso = 11
            for i in range(10):
                soma += int(numeros[i]) * peso
                peso -= 1
            resto = soma % 11
            dv2 = 0 if resto < 2 else 11 - resto
            if dv1 == int(numeros[9]) and dv2 == int(numeros[10]):
                print("CPF válido!")
            else:
                print("CPF inválido!")
