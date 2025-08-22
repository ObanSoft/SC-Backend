from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.reportes.servicioDetalleProducto import obtener_detalle_producto_servicio

detalle_bp = Blueprint('producto_detalle', __name__)

@detalle_bp.route('/producto_detalle', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def producto_detalle():
    if request.method == 'OPTIONS':
        return '', 200

    nombre = request.args.get('nombre')
    data, error = obtener_detalle_producto_servicio(nombre)

    if error:
        return jsonify({'error': error}), 400 if error == 'Falta el nombre del producto' else 500

    return jsonify(data), 200
