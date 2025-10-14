from flask import Blueprint, request, jsonify
from utils.auth_utils import token_required
from servicios.productos.servicioRegistrarProducto import registrar_producto_service

registrar_bp = Blueprint('registrarProducto', __name__)

@registrar_bp.route('/registrarProducto', methods=['POST'])
@token_required
def registrar_producto():
    data = request.get_json()
    nombre = data.get('nombre')
    precio_venta = data.get('precio_venta')
    precio_compra = data.get('precio_compra')
    cantidad = data.get('cantidad', 1)

    response, status = registrar_producto_service(nombre, precio_venta, precio_compra, cantidad)
    return jsonify(response), status
