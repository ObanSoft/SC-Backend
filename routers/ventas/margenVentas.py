from flask import Blueprint, jsonify
from app.models import db
from app.models.Venta import Venta
from utils.auth_utils import token_required
from sqlalchemy import func
from flask_cors import cross_origin

margen_ventas_bp = Blueprint('margen_ventas', __name__)

@margen_ventas_bp.route('/margen_ventas', methods=['GET',  'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def calcular_margen_ventas():
    total_ventas = db.session.query(func.sum(Venta.precio))\
        .filter(Venta.tipo_venta == 'Individual')\
        .scalar()

    if total_ventas is None:
        total_ventas = 0.0

    return jsonify({
        'mensaje': 'Margen total de ventas',
        'total_ventas_cop': float(total_ventas)
    }), 200
