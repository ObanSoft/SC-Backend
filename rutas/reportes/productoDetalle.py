from flask import Blueprint, request, jsonify
from utils.auth_utils import token_required
from servicios.reportes.servicioDetalleProducto import obtener_detalle_producto_servicio

detalle_bp = Blueprint('productoDetalle', __name__)

@detalle_bp.route('/productoDetalle', methods=['GET'])
@token_required
def producto_detalle():
    nombre = request.args.get('nombre')
    data, error = obtener_detalle_producto_servicio(nombre)

    if error:
        return jsonify({'error': error}), 400 if error == 'Falta el nombre del producto' else 500

    return jsonify(data), 200
