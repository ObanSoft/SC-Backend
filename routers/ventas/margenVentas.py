from flask import Blueprint, jsonify
from models.Venta import Venta
from utils.auth_utils import token_required
from sqlalchemy import func
from models import db

margen_ventas_bp = Blueprint('margen_ventas', __name__)

@margen_ventas_bp.route('/margen_ventas', methods=['GET'])
@token_required
def calcular_margen_ventas():
    total_ventas = db.session.query(func.sum(Venta.precio)).scalar()

    if total_ventas is None:
        total_ventas = 0.0

    return jsonify({
        'mensaje': 'Margen total de ventas',
        'total_ventas_cop': float(total_ventas)
    }), 200
