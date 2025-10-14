from flask import Blueprint, jsonify
from utils.auth_utils import token_required
from servicios.reportes.servicioTop5 import obtener_top5_mas_vendidos

top5_bp = Blueprint('top5Vendidos', __name__)

@top5_bp.route('/top5Vendidos', methods=['GET'])
@token_required
def top5_mas_vendidos():
    response, status = obtener_top5_mas_vendidos()
    return jsonify(response), status
