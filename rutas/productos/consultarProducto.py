from flask import Blueprint, jsonify
from utils.auth_utils import token_required
from servicios.productos.servicioConsultarProducto import consultar_producto as consultar_producto_service

consultar_bp = Blueprint('consultarProducto', __name__)

@consultar_bp.route('/consultarProducto/<identificador>', methods=['GET'])
@token_required
def consultar_producto(identificador):
    response, status = consultar_producto_service(identificador)
    return jsonify(response), status
