# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ...).

months = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

arrayTemperature = []
for i in range(12):
    arrayTemperature.append(float(input(f"Digite a temperatura média de {months[i]}: ")))

annualTempAvg = sum(arrayTemperature) / 12
print(f"Média anual das temperaturas: {annualTempAvg:.2f}")

for i in range(12):
    if arrayTemperature[i] > annualTempAvg:
        print(f"A temperatura de {months[i]} foi de {arrayTemperature[i]}")
