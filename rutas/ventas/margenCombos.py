from flask import Blueprint, jsonify, request
from utils.auth_utils import token_required
from servicios.ventas.servicioMargenCombos import calcular_margen_combos

margen_combos_bp = Blueprint('margenCombos', __name__)

@margen_combos_bp.route('/margenCombos', methods=['GET'])
@token_required
def margen_combos():

    response, status = calcular_margen_combos()
    return jsonify(response), status
