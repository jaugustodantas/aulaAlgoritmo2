# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

listaMeses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

dataNascimento = input("Digite sua data de nascimento no formato (dd/mm/aaaa): ")
tst = dataNascimento.split("/")
mes = int(tst[1])

print(f'Data de nascimento: {dataNascimento}')
print(f'Você nasceu em {tst[0]} de {listaMeses[mes-1]} de {tst[2]}')