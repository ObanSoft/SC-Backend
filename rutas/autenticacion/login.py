from flask import Blueprint, request, jsonify
from servicios.autenticacion.servicioInicioSesion  import logueo_usuario

login_bp = Blueprint('login', __name__)

@login_bp.route('/iniciarSesion', methods=['POST'])
def login():
    data = request.get_json()
    numero_identificacion = data.get('numero_identificacion')
    contrasena = data.get('contrasena')

    response, status = logueo_usuario(numero_identificacion, contrasena)
    return jsonify(response), status
