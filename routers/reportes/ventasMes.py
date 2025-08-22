from flask import Blueprint, jsonify
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.reportes.servicioVentasMes import obtener_ventas_por_mes

ventas_mes_bp = Blueprint('ventas_mes', __name__)

@ventas_mes_bp.route('/ventas_por_mes', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def ventas_por_mes():
    response, status = obtener_ventas_por_mes()
    return jsonify(response), status
