from flask import Blueprint, jsonify
from app.models import db
from app.models.Venta import Venta
from utils.auth_utils import token_required
from sqlalchemy import func
from flask_cors import cross_origin

margen_combos_bp = Blueprint('margen_combos', __name__)

@margen_combos_bp.route('/margen_combos', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def calcular_margen_combos():
    total_combos = db.session.query(func.sum(Venta.precio))\
        .filter(Venta.tipo_venta == 'Combo')\
        .scalar()

    if total_combos is None:
        total_combos = 0.0

    return jsonify({
        'mensaje': 'Margen total de combos',
        'total_combos_cop': float(total_combos)
    }), 200
