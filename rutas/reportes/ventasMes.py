from flask import Blueprint, jsonify
from utils.auth_utils import token_required
from servicios.reportes.servicioVentasMes import obtener_ventas_por_mes

ventas_mes_bp = Blueprint('ventasMes', __name__)

@ventas_mes_bp.route('/ventasMes', methods=['GET'])
@token_required
def ventas_por_mes():
    response, status = obtener_ventas_por_mes()
    return jsonify(response), status
