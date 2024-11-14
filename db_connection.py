import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # No tiene contraseña
            database='a_carillo'
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
            return conn
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
 