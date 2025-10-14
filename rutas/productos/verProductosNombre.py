from flask import Blueprint, jsonify, request
from utils.auth_utils import token_required
from servicios.productos.servicioBuscarNombre import buscar_productos_por_nombre_servicio

buscar_nombre_bp = Blueprint('buscarProducto', __name__)

@buscar_nombre_bp.route('/buscarProducto', methods=['GET'])
@token_required
def buscar_productos_por_nombre():

    nombre = request.args.get('nombre')
    response, status = buscar_productos_por_nombre_servicio(nombre)
    return jsonify(response), status
