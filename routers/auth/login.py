from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from services.autenticacion.servicioInicioSesion  import logueo_usuario

login_bp = Blueprint('login', __name__)

@login_bp.route('', methods=['POST', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
def login():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()
    numero_identificacion = data.get('numero_identificacion')
    contrasena = data.get('contrasena')

    response, status = logueo_usuario(numero_identificacion, contrasena)
    return jsonify(response), status
