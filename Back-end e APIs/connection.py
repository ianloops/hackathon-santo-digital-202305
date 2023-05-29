import pymssql

server = "server"
database = "AdventureWorks"
user = "sa"
password = "senha"
host="172.00.10.30"

# Função para estabelecer a conexão com o banco de dados
def connect():
    db = pymssql.connect(server=server, user=user, password=password, database=database, host=host)
    return db
