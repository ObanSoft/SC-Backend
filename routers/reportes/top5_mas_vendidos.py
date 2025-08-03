from flask import Blueprint, jsonify
from flask_cors import cross_origin
from models.Venta import Venta
from utils.auth_utils import token_required
from sqlalchemy import func

top5_bp = Blueprint('top5_vendidos', __name__)

@top5_bp.route('/top5_mas_vendidos', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def top5_mas_vendidos():
    resultados = Venta.query.with_entities(
        Venta.nombre_producto,
        func.count(Venta.id).label('cantidad')
    ).group_by(Venta.nombre_producto)\
     .order_by(func.count(Venta.id).desc())\
     .limit(5).all()

    data = [{'producto': r.nombre_producto, 'cantidad_vendida': r.cantidad} for r in resultados]
    return jsonify(data), 200
