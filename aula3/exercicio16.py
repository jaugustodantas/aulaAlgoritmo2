# Utilize uma lista para resolver o problema a seguir. 
# Uma empresa paga seus vendedores com base em comissões. 
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante

# Lista com as vendas brutas de cada vendedor
vendas = [5000, 3000, 1000, 1500, 8000, 600, 700, 1200, 9500, 2300]

# Lista de contadores para as faixas salariais:
# Índice 0 representa $200 - $299
# Índice 1 representa $300 - $399
# ...
# Índice 8 representa $1000 ou mais
contadores = [0] * 9

# Para cada venda, calcula o salário e atualiza o contador da faixa correspondente
for venda in vendas:
    salario = 200 + 0.09 * venda
    indice = int(salario // 100) - 2  # Ex: $470 => 4 (faixa $400–$499) => índice 2
    
    if indice >= 8:
        contadores[8] += 1  # $1000 ou mais
    elif indice >= 0:
        contadores[indice] += 1  # faixas normais de $200 a $999

# Faixas salariais para exibir
faixas = [
    "$200 - $299",
    "$300 - $399",
    "$400 - $499",
    "$500 - $599",
    "$600 - $699",
    "$700 - $799",
    "$800 - $899",
    "$900 - $999",
    "$1000 em diante"
]

# Exibe os resultados
for faixa, qtd in zip(faixas, contadores):
    print(f"{faixa}: {qtd} vendedor(es)")
