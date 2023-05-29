import matplotlib.pyplot as plt
import csv
import statistics

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
vendas_totais = []
with open('data/vendas-por-mes-2016.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        vendas_totais.append(int(row["value"]))

media = statistics.mean(vendas_totais)

# Configuração do gráfico
plt.plot(meses, vendas_totais, marker='o', linestyle='-', color='black')
plt.xlabel('Meses')
plt.ylabel('Vendas Totais')
plt.title('Tendência das Vendas Totais Mensais')
plt.grid(True)

# Destaque dos meses acima da media
plt.axhline(y=media, color='red', linestyle='--', label='Linha Horizontal')
for mes in range(12):
    if vendas_totais[mes] > media:
        plt.scatter(mes, vendas_totais[mes], color='red', s=100, label='Ponto Destacado')


plt.show()
