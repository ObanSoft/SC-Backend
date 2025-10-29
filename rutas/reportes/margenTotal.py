from flask import Blueprint, jsonify, request
from utils.auth_utils import token_required
from servicios.reportes.servicioMargenTotal import obtenerMargenTotalServicio

margen_total_bp = Blueprint('margenTotal', __name__)

@margen_total_bp.route('/margenTotal', methods=['GET'])
@token_required
def margen_total():
    periodo = request.args.get('periodo', 'mes') 
    año = request.args.get('año', None)

    data, error = obtenerMargenTotalServicio(periodo=periodo, año=int(año) if año else None)
    if error:
        return jsonify({'error': 'Error al obtener margen total', 'detalle': error}), 500

    return jsonify({'margen_total': data}), 200
