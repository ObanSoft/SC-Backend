from werkzeug.security import check_password_hash
from app.models.Usuario import Usuario
import jwt
import datetime
from flask import current_app

def logueo_usuario (numero_identificacion: str, contrasena: str):
    if not numero_identificacion or not contrasena:
        return {"error": "Faltan datos obligatorios"}, 400

    try:
        user = Usuario.query.filter_by(numero_identificacion=numero_identificacion).first()

        if user and check_password_hash(user.contrasena, contrasena):
            payload = {
                "user_id": user.id,
                "numero_identificacion": user.numero_identificacion,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            }
            token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
            return {"token": token}, 200
        else:
            return {"error": "Credenciales inválidas"}, 401

    except Exception as e:
        return {"error": str(e)}, 500
