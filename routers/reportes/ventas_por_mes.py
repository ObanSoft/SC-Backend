from flask import Blueprint, jsonify
from flask_cors import cross_origin
from models.Venta import Venta
from utils.auth_utils import token_required
from sqlalchemy import extract, func
from calendar import month_name

ventas_mes_bp = Blueprint('ventas_mes', __name__)

@ventas_mes_bp.route('/ventas_por_mes', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def ventas_por_mes():
    resultados = Venta.query.with_entities(
        extract('year', Venta.fecha_venta).label('anio'),
        extract('month', Venta.fecha_venta).label('mes'),
        func.count().label('cantidad'),
        func.sum(Venta.precio).label('total')
    ).group_by('anio', 'mes').order_by('anio', 'mes').all()

    data = [
        {
            'anio': int(r.anio),
            'mes': month_name[int(r.mes)],  
            'cantidad_vendida': r.cantidad,
            'total_ventas': float(r.total)
        } for r in resultados
    ]
    return jsonify(data), 200

