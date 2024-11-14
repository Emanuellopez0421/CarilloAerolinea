from flask import Flask
import os
from routes import app_routes  # Importamos el Blueprint desde routes.py

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Registrar el Blueprint
app.register_blueprint(app_routes)

if __name__ == '__main__':
    app.run(debug=True)