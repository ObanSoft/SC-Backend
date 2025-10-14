from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from utils.auth_utils import token_required
from servicios.productos.servicioCantidadProductos import cantidad_productos_service

cantidad_bp = Blueprint('verCantidadProducto', __name__)

@cantidad_bp.route('/verCantidadProducto', methods=['GET'])
@token_required
def cantidad_productos_en_inventario():
    response, status = cantidad_productos_service()
    return jsonify(response), status
