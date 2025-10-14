from flask import Blueprint, jsonify, request
from utils.auth_utils import token_required
from servicios.ventas.servicioMargenVentas import calcular_margen_ventas

margen_ventas_bp = Blueprint('margenVentas', __name__)

@margen_ventas_bp.route('/margenVentas', methods=['GET'])
@token_required
def margen_ventas():

    response, status = calcular_margen_ventas()
    return jsonify(response), status
