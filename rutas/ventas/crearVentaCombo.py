from flask import Blueprint, request, jsonify
from utils.auth_utils import token_required
from servicios.ventas.servicioCrearCombo import registrar_combo

crear_venta_combo_bp = Blueprint('crearVentaCombo', __name__)

@crear_venta_combo_bp.route('/crearVentaCombo', methods=['POST'])
@token_required
def crear_venta_combo():
    data = request.get_json()
    nombre_combo = data.get('nombre_combo')
    productos = data.get('productos')
    vendido_por = data.get('vendido_por')
    metodo_pago = data.get('metodo_pago')

    response, status = registrar_combo(nombre_combo, productos, vendido_por, metodo_pago)
    return jsonify(response), status
