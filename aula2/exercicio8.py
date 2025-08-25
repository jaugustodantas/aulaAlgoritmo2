senha = input("Digite um senha: A senha deve ter no mínimo 1 número, uma letra maiuscula e no mínimo 8 caracteres: ")
#tst = len(senha)
maiuscula = None
numero = None
while True:
    if len(senha) < 8:
        print("A senha deve ter no mínimo 8 digitos")
        break

    for digito in senha:
        if digito.isupper():
            maiuscula = True
        if digito.isdigit():
            numero = True

    if maiuscula == True and numero == True:
        print("Senha forte criada com sucesso")
        break
    else:
        print("A senha deve ter no mínimo 1 letra maiuscula e 1 número")
        break