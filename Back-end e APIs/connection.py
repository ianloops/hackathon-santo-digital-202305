import pyodbc

server = "MSSQL"


# Função para estabelecer a conexão com o banco de dados
def connect():
    db = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server="+server+";"
                        "Database=AdventureWorks;"
                        "Trusted_connection=yes;")
    return db
