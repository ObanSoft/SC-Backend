from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from servicios.autenticacion.servicioRegistro import servicio_registrar_usuario

usuarios_bp = Blueprint('registro', __name__)

@usuarios_bp.route('/registrarUsuario', methods=['POST'])
def registrar_usuario():
    data = request.get_json() or {}
    resp, status = servicio_registrar_usuario(
        numero_identificacion=data.get('numero_identificacion'),
        contrasena=data.get('contrasena'),
    )
    return jsonify(resp), status
