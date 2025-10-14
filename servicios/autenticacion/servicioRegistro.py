from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from app.models import db
from app.models.Usuario import Usuario

def servicio_registrar_usuario (numero_identificacion: str, contrasena: str):
    if not numero_identificacion or not contrasena:
        return {"error": "Faltan datos obligatorios"}, 400

    hashed_password = generate_password_hash(contrasena)

    user = Usuario(
        numero_identificacion=numero_identificacion,
        contrasena=hashed_password,
    )
    db.session.add(user)
    try:
        db.session.commit()
        return {"mensaje": "Usuario registrado exitosamente"}, 201
    except IntegrityError:
        db.session.rollback()
        return {"error": "El número de identificación ya existe"}, 409
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500


