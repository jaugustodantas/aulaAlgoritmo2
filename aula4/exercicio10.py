# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
unidade = ['zero','um','dois','três','quatro','cinco','seis','sete','oito','nove']
dezena = ['zero','dez','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
casaDez = ['dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
numIndex = 0
numero = input("Digite um número entre 01 e 99: ")
if numero[0]=='0':
    numIndex = int(numero[1])
    print(f'{unidade[numIndex]}')
elif numero[0]=='1':
    numIndex = int(numero[1])
    print(f'{casaDez[numIndex]}')
elif int(numero[0]) >= '2':
    print(f'{dezena[int(numero[0])]} e {unidade[int(numero[1])]}')
