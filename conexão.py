import mysql.connector
from mysql.connector import errorcode
import datetime

try: 
    db_connection = mysql.connector.connect(host='localhost', user='yamacinelli', password='765589', database='teste_banco_de_dados')
    print("Conexão com o Banco de Dados realizada!")

    if db_connection.is_connected():
        db_informações = db_connection.get_server_info()
        print(f"Conectado ao servidor MY SQL: {db_informações}")
        cursor = db_connection.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
                                                                # CRIAÇÃO DE MENU
    print(f"""\n {'='*20} MENU {'='*20}\n
    [1] Inserir\n
    [2] Alterar\n
    [3] Deletar\n
    [4] SAIR\n""")

    opcao = int(input("Digite um opção: "))
                                                                # INPUT DOS VALORES PELO PRÓPRIO USUÁRIO
    if(opcao == 1):
        cliente_nome = input("Nome do Cliente: ")
        cliente_sexo = input("Sexo do Cliente (m [masculino] ------ f [feminino]): ")
        cliente_sexo = cliente_sexo.lower()          # TRAZ PARA MINÚSCULO CASO O USUÁRIO DIGITE EM MAIÚSCULO

        dados = '\'' + cliente_nome + '\'' + ',\'' + cliente_sexo + '\'' + '\''       # VARIÁVEL RESPONSÁVEL PELA CONCATENAÇÃO DOS VALORES

        inserir_cliente = f"""INSERT INTO cliente
                    (nome, sexo)
                VALUES ({dados})"""            # SPRINT COM COMANDOS EM LINGUAGEM SQL

        cursor.execute(inserir_cliente)        # PROPRIEDADE RESPONSÁVEL PELA EXECUÇÃO DA SPRINT 'inserir_cliente'
        db_connection.commit()                 # PROPRIEDADE QUE GRAVARÁ OS VALORES EXECUTADOS NO DB
        print(f"Foram inseridos {cursor.rowcount} registros na tabela!")         # ESTA PROPRIEDADE RETORNARÁ O Nº DE LINHAS QUE FORAM ADICIONADAS AO DB
        cursor.close()
            
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de Dados não existe!")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Nome de usuário ou senho incorretos!")
    else:
        print(error)
        db_connection.close()
finally:
    if((db_connection.is_connected())):
        db_connection.close()
        print("Conexão com o MySQL finalizada!")