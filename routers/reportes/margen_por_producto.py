from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.reportes.servicioMargenProducto import obtener_margen_por_producto_servicio

margen_bp = Blueprint('margen_producto', __name__)

@margen_bp.route('/margen_por_producto', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def margen_por_producto():
    if request.method == 'OPTIONS':
        return '', 200

    data, error = obtener_margen_por_producto_servicio()
    if error:
        return jsonify({'error': 'Error al obtener margen por producto', 'detalle': error}), 500

    return jsonify({'margen_por_producto': data}), 200
