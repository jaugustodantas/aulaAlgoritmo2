def calculaValor (n1,n2):
    return f'{n1} x {n2} = {n1*n2}'


numero = int(input("Digite um número de 1 a 10: "))

for x in range (1,11):
    print(calculaValor(numero,x))