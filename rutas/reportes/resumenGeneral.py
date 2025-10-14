from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from utils.auth_utils import token_required
from servicios.reportes.servicioResumenGeneral import obtener_resumen_general_servicio

resumen_bp = Blueprint('resumenGeeneral', __name__)

@resumen_bp.route('/resumenGeneral', methods=['GET'])
@token_required
def resumen_general():
    data, error = obtener_resumen_general_servicio()
    if error:
        return jsonify({'error': 'Error al generar resumen', 'detalle': error}), 500

    return jsonify(data), 200
