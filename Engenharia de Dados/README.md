# Engenharia de Dados

### Apresentação
---

Para a realização deste desafio, foi realizado o SQL SERVER 2016 e o SSMS para criar o banco importando as <br>
tabelas dos arquivos .csv fornecidos. A escolha foi feita considerando afinidade com a ferramenta. 

O arquivo **Modelo-Entidade-Relacionamento.png** é um esboço de um modelo entidade relacionamento <br>
utilizado para melhor compreensão do dados. 

O arquivo **AdventureWorks.bak** é um backup que pode ser utilizado para restaurar o banco já populado no <br>
SQL SERVER. O link a seguir demonstra como pode ser feita essa recuperação pelo assistente do SSMS
https://learn.microsoft.com/pt-br/sql/relational-databases/backup-restore/quickstart-backup-restore-database?view=sql-server-ver16#restore-a-backup

A pasta **sqls e csvs** contem as queries propostas no desafio, além de mais algumas elaboradas que puderam<br>
ser utilizadas no desafio de back-end e na tarefa extra. Também contem o respectivo arquivo .csv resultado de cada query

A pasta **graficos** contem visualizações de dados desenvolvidos em python. Um arquivo **requirements.txt**<br>
e mais uma pasta com arquivos .csv que foram utilizados para plotar os gráficos.

### Resoluções
---
##### Quais são os 10 produtos mais vendidos (em quantidade) na categoria "Bicicletas"?
Utilizando Union foi possível juntar as 3 tabelas referente a vendas em uma só, para então utilizar de joins para <br>
obter os dados necessários para filtrar a categoria. Feito isso somamos a quantidade de pedidos agrupando por<br>
produto e selecionamos os 10 primeiros resultados em ordem decrescente

##### Qual é o cliente que tem o maior número de pedidos realizados?
Utilizando basicamente a mesma estrategia da questão anterior, mas dessa vez o join é com o cliente, para que<br>
possamos agrupar por cliente e então selecionar o primeiro resultado em ordem decrescente

##### Em qual mês do ano ocorrem mais vendas (em valor total)?
Para essa questão foi utilizado apenas as vendas do último ano fiscal(2016). Fazendo um Join com a tabela de <br>
produtos, podemos obter o valor de cada um e multiplicar pela quantidade do pedido, obtendo o custo do <br>
pedido. Agrupamos então por mês e selecionamos o que teve mais vendas.

##### ~~Quais vendedores tiveram vendas com valor acima da média no último ano fiscal?~~
##### Quais regiões tiveram vendas com valor acima da média no último ano fiscal?
Primeiro foi necessário criar uma subquery que trouxesse o total de vendas de cada região em 2016<br>
Essa subquery é chamada num select simples e na cláusula where passamos a mesma subquery para<br>
buscar o valor da média, para que possamos criar a condição de "total>media" na query principal

##### Extra: Elabore e responda uma pergunta de negócio do seu interesse.
##### Quais regiões não tiveram devoluções?
Utilizando um select das devoluções com um RIGHT JOIN nas regiões, é possível trazer todas as regiões, <br>
mesmo as que não possuem devoluções. Usando a cláusula HAVING podemos filtrar apenas as regiões <br>
em que não houve nenhuma devolução.

## Gráficos
### Imports utilizados
---
*pyplot*: Utilizado para plotar os gráficos<br>
*csv*: Utilizado para leitura dos arquivos csv<br>
*statistics*: Utilizado para obter média aritmética<br>
*pandas*: Utilizado para criação de um DataFrame<br>
*seaborn*: Utilizado para criar o mapa de calor

### Instalando as dependências
---

Para instalar as dependências, com o pip instalado, basta executar:

```bash
$ pip install -r requirements.txt 
```

E então executar a visualização desejada(em ambiente Windows): 
-
```bash
$ py.exe .\visualizacao1.py
$ py.exe .\visualizacao2.py
$ py.exe .\visualizacao3.py
```