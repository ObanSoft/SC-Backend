from flask import Blueprint, jsonify, request
from utils.auth_utils import token_required
from servicios.reportes.servicioMargenProducto import obtener_margen_por_producto_servicio

margen_bp = Blueprint('margenPorProducto', __name__)

@margen_bp.route('/margenPorProducto', methods=['GET'])
@token_required
def margen_por_producto():
    data, error = obtener_margen_por_producto_servicio()
    if error:
        return jsonify({'error': 'Error al obtener margen por producto', 'detalle': error}), 500

    return jsonify({'margen_por_producto': data}), 200
