from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash
import mysql.connector

usuarios_bp = Blueprint('registro', __name__)

@usuarios_bp.route('/registro', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    numero_identificacion = data.get('numero_identificacion')
    contrasena = data.get('contrasena')

    if not numero_identificacion or not contrasena:
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    hashed_password = generate_password_hash(contrasena)

    try:
        conn = mysql.connector.connect(
            host=current_app.config["DB_HOST"],
            user=current_app.config["DB_USER"],
            password=current_app.config["DB_PASSWORD"],
            database=current_app.config["DB_NAME"]
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (numero_identificacion, contrasena) VALUES (%s, %s)",
            (numero_identificacion, hashed_password)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201
    except mysql.connector.IntegrityError:
        return jsonify({"error": "El número de identificación ya existe"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500