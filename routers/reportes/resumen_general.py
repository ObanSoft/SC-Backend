from flask import Blueprint, jsonify
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.reportes.servicioResumenGeneral import obtener_resumen_general_servicio

resumen_bp = Blueprint('resumen_general', __name__)

@resumen_bp.route('/resumen_general', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def resumen_general():
    if request.method == 'OPTIONS':
        return '', 200

    data, error = obtener_resumen_general_servicio()
    if error:
        return jsonify({'error': 'Error al generar resumen', 'detalle': error}), 500

    return jsonify(data), 200
