# Archivo de rutas para la aplicación
from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from db_connection import get_db_connection  # Asegúrate de que esta función devuelve una conexión a la base de datos

app_routes = Blueprint('app_routes', __name__)

# Página de inicio
@app_routes.route('/')
def index():
    return render_template('index.html')