from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.productos.servicioRegistrarProducto import registrar_producto_service

registrar_bp = Blueprint('registrar_producto', __name__)

@registrar_bp.route('/registrar_producto', methods=['POST', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def registrar_producto():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()
    nombre = data.get('nombre')
    precio_venta = data.get('precio_venta')
    precio_compra = data.get('precio_compra')
    cantidad = data.get('cantidad', 1)

    response, status = registrar_producto_service(nombre, precio_venta, precio_compra, cantidad)
    return jsonify(response), status
