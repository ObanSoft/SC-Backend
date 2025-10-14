from flask import Blueprint, jsonify, request
from utils.auth_utils import token_required
from servicios.ventas.servicioVentasNombre import obtener_ventas_por_nombre_service

ventas_por_nombre_bp = Blueprint('ventasPorNombre', __name__)

@ventas_por_nombre_bp.route('/ventasPorNombre/<nombre_producto>', methods=['GET'])
@token_required
def ventas_por_nombre(nombre_producto):

    response, status = obtener_ventas_por_nombre_service(nombre_producto)
    return jsonify(response), status
