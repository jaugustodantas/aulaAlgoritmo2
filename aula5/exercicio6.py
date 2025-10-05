# Faça um programa que converta a notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.

# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.

# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas às vezes que desejar.

#lista das horas do dia

manha = [0,1,2,3,4,5,6,7,8,9,10,11]
tarde = [12,13,14,15,16,17,18,19,20,21,22,23]

def converte_hora (hora):
    hour = hora.split(":")  #cria um array com hora e minuto 
    teste = int(hour[0])
    if teste in manha:
        #horaCorrigida = manha.index(teste)
        return f'{manha.index(teste)}:{hour[1]} A.M'
    elif teste in tarde:
        horaCorrigida = tarde.index(teste)
        if horaCorrigida == 0:
            horaCorrigida +=12
        return f'{horaCorrigida}:{hour[1]} P.M'
    else:
        return f"Valor inválido"

hour = input("Digite as horas no formato 24 horas Ex. 13:58 : ")
print(converte_hora(hour))