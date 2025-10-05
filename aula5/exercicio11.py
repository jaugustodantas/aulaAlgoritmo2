# Data com mês por extenso.
# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mes_por_extenso de AAAA.
# Opcionalmente, valide a data e retorne None caso a data seja inválida.

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

def conversorData (data):
    separador = data.split("/")
    mesNumerico = int(separador[1])
    if int(separador[0]) <= 0 or int(separador[0]) > 31: #checa se o númro do dia é válido
        return f'O valor do dia tem que ser maior que 0 e menor que 31. Data inválida'
    
    if (mesNumerico ==2) and (int(separador[0])>29): #checa se o mês de fevereiro tem no máximo 29 dias
        return f'O mes de fevereiro não pode ter mais que 29 dias. Data inválida'
    
    if mesNumerico > 12: #testa se o mês só vá até o mês 12
        return f'O ano só pode ter 12 meses. Data inválida'

    mesExtenso = meses[mesNumerico-1]
    return f'{separador[0]} de {mesExtenso} de {separador[2]}'

data = input("Digite uma data no formato dd/MM/AAAA: ")
print(conversorData(data))