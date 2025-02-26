import mysql.connector
from config import MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE

def get_connection():
    returm mysql.connector.connect(
        host = MYSQL_HOST
        user = MYSQL_USER
        password = MYSQL_PASSWORD
        database = MYSQL_DATABASE


    )


    def create_user(NOME, TELEFONE, EMAIL, USUARIO, SENHA):
        conn = get_connection()
        cursor = conn.cursor()
        query = "inserit usuario(NOME,TELEFONE,EMAIL,USUARIO,SENHA) VALUES(%5,%5,%5,%5,%5)"

        cursor.execute(query,(NOME,TELEFONE,EMAIL,USUARIO,SENHA))
        conn.commit()
        cursor.close()
        conn.close()
        

        def create_user(NOME, TELEFONE, EMAIL, USUARIO, SENHA):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM usuario"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()





        def create_user(NOME, TELEFONE, EMAIL, USUARIO, SENHA):
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE usuario SET nome=%s, TELEFONE=%s, EMAIL=%s,USUARIO=%s,SENHA=%s WHERE idusuario = %s)"

        cursor.execute(query,(NOME,TELEFONE,EMAIL,USUARIO,SENHA,USER_ID))
        conn.commit()
        cursor.close()
        conn.close()
        

        def create_user(NOME, TELEFONE, EMAIL, USUARIO, SENHA):
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE usuario SET nome=%s, TELEFONE=%s, EMAIL=%s,USUARIO=%s,SENHA=%s WHERE idusuario = %s)"

        cursor.execute(query,(NOME,TELEFONE,EMAIL,USUARIO,SENHA))
        conn.commit()
        cursor.close()
        conn.close()
        


        def delete(NOME, TELEFONE, EMAIL, USUARIO, SENHA):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM usuario WHERE idusuario=%s)"

        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        
        
