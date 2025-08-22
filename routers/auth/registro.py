from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from services.autenticacion.servicioRegistro import registrar_usuario

usuarios_bp = Blueprint('registro', __name__)

@usuarios_bp.route('/registro', methods=['POST'])
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
def registrar_usuario():
    data = request.get_json() or {}
    resp, status = registrar_usuario(
        numero_identificacion=data.get('numero_identificacion'),
        contrasena=data.get('contrasena'),
    )
    return jsonify(resp), status
