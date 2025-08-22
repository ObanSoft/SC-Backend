from flask import Blueprint, jsonify
from utils.auth_utils import token_required
from flask_cors import cross_origin
from services.productos.servicioCambioEstado import cambiar_estado_producto as cambiar_estado_producto_service

cambio_estado_bp = Blueprint('cambio_estado', __name__)

@cambio_estado_bp.route('/cambiar_estado/<identificador_unico>', methods=['PUT', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def cambiar_estado_producto(identificador_unico):
    response, status = cambiar_estado_producto_service(identificador_unico)
    return jsonify(response), status
