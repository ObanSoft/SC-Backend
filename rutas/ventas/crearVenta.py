from flask import Blueprint, request, jsonify
from utils.auth_utils import token_required
from servicios.ventas.servicioCrearVenta import registrar_ventas

crear_venta_bp = Blueprint('crearVenta', __name__)

@crear_venta_bp.route('/crearVenta', methods=['POST'])
@token_required
def crear_venta():

    data = request.get_json()
    nombre_producto = data.get('nombre_producto')
    cantidad = data.get('cantidad', 1)
    vendido_por = data.get('vendido_por')
    metodo_pago = data.get('metodo_pago')

    response, status = registrar_ventas(nombre_producto, cantidad, vendido_por, metodo_pago)
    return jsonify(response), status
