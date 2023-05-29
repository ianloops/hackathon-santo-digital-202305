import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


region = []
month = []
saleTotal = []

with open('data/vendas-por-mes-por-regiao.csv', newline='', encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        region.append(row["Region"])
        saleTotal.append(int(row["salesVolume"]))
        month.append(int(row["month"]))

dados = {
    'Região': region,
    'Mês': month,
    'Vendas': saleTotal
}


df = pd.DataFrame(dados)

df_heatmap = df.pivot_table(index='Região', columns='Mês', values='Vendas')

# Criar o mapa de calor
plt.figure(figsize=(10, 6))
sns.heatmap(df_heatmap, annot=True, cmap='YlGnBu', fmt='.0f')

plt.title('Vendas por Região e Mês')
plt.xlabel('Mês')
plt.ylabel('Região')

plt.show()
