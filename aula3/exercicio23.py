# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. 
# Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

# usuarios.txt
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres.

# A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa.
# A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. 
# O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
def formatacao (total,kwargs):
    return f"{str(kwargs['id']):<4}{kwargs['nome']:<15}{kwargs['espaco']:>20.2f}MB {((kwargs['espaco']/total)*100):>12.2f}% \n" 

dictModel = {
    "id":None,
    "nome":None,
    "espaco": None
}
identificador = 1
ocorrencias = []
listaDicionario = []
acumulador = 0
with open('usuarios.txt','r', encoding='utf-8') as arquivo:  #le o arquivo usuários .txt
    for linha in arquivo:
        ocorrencias.append(linha)

for o in ocorrencias:
    novoDicionario = {}
    teste = o.split()
    for key in dictModel:
        if key == 'id':
            novoDicionario[key] = identificador
        elif key == 'nome':
            novoDicionario[key] = teste[0]
        else:
            novoDicionario[key] = int(teste[1])
    identificador+=1
    listaDicionario.append(novoDicionario)

for u in listaDicionario:
   valor =  u['espaco']
   valor = valor / (1024**2)
   u['espaco'] = valor
   acumulador += valor

with open("relatorio.txt", "w") as arquivo:
    arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários \n")
    arquivo.write("-" * 60 +"\n")
    for u in listaDicionario:
        arquivo.write(formatacao(acumulador,u))
    arquivo.write(f'Espaço total ocupado {acumulador:.2f} MB \n')
    arquivo.write(f'Espaço médio ocupado {acumulador/len(listaDicionario):.2f} MB')
