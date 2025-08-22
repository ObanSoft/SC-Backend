from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.productos.servicioDisolverCombo import disolver_combo as disolver_combo_service

disolver_combo_bp = Blueprint('disolver_combo', __name__)

@disolver_combo_bp.route('/disolverCombo', methods=['POST', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def disolver_combo():
    data = request.get_json()
    identificador_combo = data.get('identificador_combo')
    response, status = disolver_combo_service(identificador_combo)
    return jsonify(response), status
