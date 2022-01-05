from mysql.connector import (connection)
db_connection = connection.MySQLConnection(host='localhost', user='yamacinelli', password='765589', database='teste_banco_de_dados')
if db_connection.is_connected():
    db_informações = db_connection.get_server_info()
    print(f"Conectado ao servidor MY SQL: {db_informações}")
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print(f"Conectado ao banco de dados: {linha}")
if db_connection.is_connected():
    cursor.close()
    db_connection.close()
    print("Conexão ao MY SQL encerrada.")