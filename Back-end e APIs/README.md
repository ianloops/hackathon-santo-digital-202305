# Back-end e API

### Tecnologias Utilizadas
*Python*: Linguagem utilizada<br>
*SQL SERVER*: Banco utilizado<br>
*FastAPI*: Utilizado para desenvolvimento da API documentada com Swagger<br>
*pyodbc*: Utilizado para conectar com o banco<br>
*pydantic*: Utilizado para criar o modelo de dados do produto<br>
*uvicorn*: Servidor onde a API executa

### Requisitos
*Python instalado*<br>
*Pip instalado*<br>
*Instância SQL SERVER com o banco restaurado pelo arquivo **AdventureWorks.bak**(Mesmo utilizado para <br>
rodar os arquivos sql do desafio de Engenharia de dados)*

### Arquivos
*AdventureWorks.bak*: Arquivo de backup do banco<br>
*connection.py*: Arquivo de configuração para conectar com o banco<br>
*main.py*: Arquivo principal com a chamada do app e rotas da API<br>
*product.py*: Classe para representar o modelo de dados do produto<br>
*requirements.txt*: Arquivo com dependências necessárias para funcionamento da API<br>
*service.py*: Camada de serviço, definição das funções chamados por cada rota

### Instalando as dependências
---

Para instalar as dependências com o pip basta executar:

```bash
$ pip install -r requirements.txt 
```

### Configurando conexão com banco
---

Acesse o arquivo **connection.py** e altere o valor da variável "server" para o nome de sua instância SQL Server

### Executando a API
---

Para executar a API use o comando:

```bash
$ uvicorn main:app
```

Assim a aplicação vai estar no endereço `http://localhost:8000`.

### Testando a API
---

Em relação aos testes, eles podem ser feitos utilizando a interface do Swagger, presente por padrão no FastAPI. Para acessar essa interface basta entrar no endereço `http://localhost:8000/docs`.

