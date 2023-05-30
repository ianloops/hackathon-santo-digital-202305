# Back-end e API

### Tecnologias Utilizadas
*Python*: Linguagem utilizada<br>
*SQL SERVER*: Banco utilizado<br>
*FastAPI*: Utilizado para desenvolvimento da API documentada com Swagger<br>
*pymssql*: Utilizado para conectar com o banco<br>
*pydantic*: Utilizado para criar o modelo de dados do produto<br>
*uvicorn*: Servidor onde a API executa<br>
*docker-compose*: Utilizado para subir a aplicação em containers

### Requisitos
*Docker instalado com Docker-compose*

### Arquivos
*AdventureWorks.bak*: Arquivo de backup do banco<br>
*connection.py*: Arquivo de configuração para conectar com o banco<br>
*main.py*: Arquivo principal com a chamada do app e rotas da API<br>
*product.py*: Classe para representar o modelo de dados do produto<br>
*requirements.txt*: Arquivo com dependências necessárias para funcionamento da API<br>
*service.py*: Camada de serviço, definição das funções chamados por cada rota<br>
*Dockerfile*: Arquivo Dockerfile utilizado para subir a aplicação com Docker<br>
*docker-compose.yml*: Arquivo de configuração dos containers para API e Banco<br>
*restore.sql*: Arquivo de script para importação do banco <br>
*entrypoint.sh*: Arquivo shellscript para executar a importação do banco

### Executando docker-compose

```bash
$ docker-compose up 
```
A aplicação irá subir junto ao banco de dados em dois containers, pode levar cerca de 2 min para importação do banco <br>
Aguarde pela mensagem ao fim da importação do banco

 Setting database option READ_WRITE to ON for database 'AdventureWorks'.

Assim a aplicação vai estar no endereço `http://localhost:8000`.

### Testando a API
---

Em relação aos testes, eles podem ser feitos utilizando a interface do Swagger, presente por padrão no FastAPI. <br>
Para acessar essa interface basta entrar no endereço `http://localhost:8000/docs`.

