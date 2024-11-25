from db_connection import get_db_connection

def get_user_by_username(username):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuario WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

def create_user(nombre, correo, username, password, role):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO usuario (nombre, correo, username, password, role) VALUES (%s, %s, %s, %s, %s)", (nombre, correo, username, password, role))
    connection.commit()
    cursor.close()
    connection.close()

def get_vuelos():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vueloandm")
    vuelos = cursor.fetchall()
    cursor.close()
    connection.close()
    return vuelos

def get_pagos():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pagos")
    pagos = cursor.fetchall()
    cursor.close()
    connection.close()
    return pagos

# Agrega más funciones para obtener y gestionar datos en la base de datos
