from flask import Blueprint, jsonify
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.productos.servicioEliminarProducto import eliminar_producto as eliminar_producto_service

eliminar_bp = Blueprint('eliminar_producto', __name__)

@eliminar_bp.route('/eliminar_producto/<identificador>', methods=['DELETE', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def eliminar_producto(identificador):
    response, status = eliminar_producto_service(identificador)
    return jsonify(response), status
