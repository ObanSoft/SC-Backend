from flask import Blueprint, jsonify
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.reportes.servicioTop5 import obtener_top5_mas_vendidos

top5_bp = Blueprint('top5_vendidos', __name__)

@top5_bp.route('/top5_mas_vendidos', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def top5_mas_vendidos():
    response, status = obtener_top5_mas_vendidos()
    return jsonify(response), status
