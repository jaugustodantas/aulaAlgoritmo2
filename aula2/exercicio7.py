palavra = input("Deigite uma palavra ")

for letra in palavra:
    if letra in ("a","e","i","o","u"):
        print(f'{letra} - vogal')
    else:
        print(letra)

