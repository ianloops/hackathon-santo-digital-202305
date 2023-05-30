import pymssql

server = "mssql"
database = "AdventureWorks"
user = "sa"
password = "@dv202305"
host = "mssql"


# Função para estabelecer a conexão com o banco de dados
def connect():
    db = pymssql.connect(server=server, user=user, password=password, database=database, host=host)
    return db
