# Faça um programa com uma função chamada soma_imposto.
# A função possui dois parâmetros formais: taxa_imposto, que é a quantia de imposto sobre vendas expressas em porcentagem, e custo, que é o custo de um item antes do imposto.
# A função "altera" o valor de custo para incluir o imposto sobre vendas.

def soma_imposto (taxa_imposto,custo):
    return f'{taxa_imposto * custo}'


taxa = float(input("Digite o valor da taxa: "))
custo = float(input("Digite o custo do produto: "))
print(soma_imposto(taxa,custo))