import matplotlib.pyplot as plt
import csv

quantity = []
productKey = []
with open('data/10 mais vendidos em bicicleta sem nome.csv', newline='', encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        productKey.append(row["productKey"])
        quantity.append(int(row["quantity"]))


# Configuração do gráfico
plt.bar(productKey, quantity, linestyle='-', color='green')
plt.xlabel('Meses')
plt.ylabel('Vendas Totais')
plt.title('Tendência das Vendas Totais Mensais')
plt.grid(True)

plt.show()
