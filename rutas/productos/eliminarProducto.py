from flask import Blueprint, jsonify
from utils.auth_utils import token_required
from servicios.productos.servicioEliminarProducto import eliminar_producto as eliminar_producto_service

eliminar_bp = Blueprint('eliminarProducto', __name__)

@eliminar_bp.route('/eliminarProducto/<identificador>', methods=['DELETE'])
@token_required
def eliminar_producto(identificador):
    response, status = eliminar_producto_service(identificador)
    return jsonify(response), status
