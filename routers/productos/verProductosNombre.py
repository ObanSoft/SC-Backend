from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.productos.servicioBuscarNombre import buscar_productos_por_nombre_servicio

buscar_nombre_bp = Blueprint('buscar_productos', __name__)

@buscar_nombre_bp.route('/buscar', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def buscar_productos_por_nombre():
    if request.method == 'OPTIONS':
        return '', 200

    nombre = request.args.get('nombre')
    response, status = buscar_productos_por_nombre_servicio(nombre)
    return jsonify(response), status
