from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash
from models.Usuario import db, Usuario
from flask_cors import cross_origin
import jwt
import mysql.connector
import datetime

login_bp = Blueprint('login', __name__)

@login_bp.route('', methods=['POST', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
def login():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()
    numero_identificacion = data.get('numero_identificacion')
    contrasena = data.get('contrasena')

    if not numero_identificacion or not contrasena:
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    try:
        conn = mysql.connector.connect(
            host=current_app.config["DB_HOST"],
            user=current_app.config["DB_USER"],
            password=current_app.config["DB_PASSWORD"],
            database=current_app.config["DB_NAME"]
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, numero_identificacion, contrasena FROM usuarios WHERE numero_identificacion = %s",
            (numero_identificacion,)
        )
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user["contrasena"], contrasena):
            payload = {
                "user_id": user["id"],
                "numero_identificacion": user["numero_identificacion"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            }
            token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")

            return jsonify({"token": token}), 200
        else:
            return jsonify({"error": "Crendenciales Invalidas"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500
