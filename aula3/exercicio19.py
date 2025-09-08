# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
# O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
# Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
# Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. 
# O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
import os
import time
from collections import Counter

def clearScreen ():
    os.system('cls' if os.name =='nt' else 'clear')  #chama a limpeza de tela dependendo do sistema operacional

def cleaning(wTime):
    time.sleep(wTime)  #põe o sistema em espera por x segundos para chamar a próxima função 
    clearScreen()

osDict ={
    1:"Windows Server",
    2:"Unix",
    3:"Linux",  
    4:"Netware",
    5:"Mac OS",
    6:"Outros"
}

votes = []
while True:
    print(" As opções da votação são: \n 0- Sair \n 1- Windows Server \n 2- Unix \n 3- Linux \n 4- Netware \n 5- Mac OS \n 6- Outro")
    number = int(input("Digite o número que você quer votar: "))
    if number == 0:
        break
    elif number > 6:
        print("Valor digitado inválido")
        cleaning(5)
        continue

    cleaning(0)    
    votes.append(number)

totalVotes = Counter(votes)  #funão para contar o número de cada ocorrência 
arrayLen = len(votes)

test = 0
print(f'{'Sistema Operacional':<20}{'Votos':<15}{'%':<5}')
for number,occurence in totalVotes.items():  #corre os numeros e tras a contagem desses numeros
    osName = osDict[number]
    o = occurence
    percent = 100*(occurence/arrayLen)
    print(f'{osName:<20}{o:<15}{percent:<5.1f}%')  #o < serve para dar o espaçamento no print
    if o> test:
        dictFinalResult ={        #cria um dicionário com as informações do sistema operacional ganhador
            "os": osName,
            "total":o,
            "p":percent
        }
        test = o

print(f'O Sistema Operacional mais votado foi o {dictFinalResult["os"]}, com {dictFinalResult["total"]} votos, correspondendo a {dictFinalResult["p"]:.1f}% dos votos.')