from flask import Blueprint, jsonify
from utils.auth_utils import token_required
from servicios.productos.servicioCambioEstado import cambiar_estado_producto as cambiar_estado_producto_service

cambio_estado_bp = Blueprint('cambiarEstado', __name__)

@cambio_estado_bp.route('/cambiarEstado/<identificador_unico>', methods=['PUT'])
@token_required
def cambiar_estado_producto(identificador_unico):
    response, status = cambiar_estado_producto_service(identificador_unico)
    return jsonify(response), status
