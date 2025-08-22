from flask import Blueprint, jsonify
from app.models import db
from app.models.Venta import Venta
from utils.auth_utils import token_required
from flask_cors import cross_origin

ventas_por_nombre_bp = Blueprint('ventas_por_nombre', __name__)

@ventas_por_nombre_bp.route('/producto/nombre/<nombre_producto>', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def obtener_ventas_por_nombre(nombre_producto):
    nombre_limpio = nombre_producto.strip()  

    ventas = Venta.query.filter_by(nombre_producto=nombre_limpio).all()

    if not ventas:
        return jsonify({'error': f'No se encontraron ventas para "{nombre_limpio}"'}), 404

    return jsonify({
        'nombre_producto': nombre_limpio,
        'total_ventas': len(ventas),
        'ventas': [
            {
                'identificador_unico': v.identificador_unico,
                'precio': float(v.precio),
                'fecha_venta': v.fecha_venta.strftime('%Y-%m-%d %H:%M:%S'),
                'tipo_venta': v.tipo_venta,
                'vendido_por': v.vendido_por,
            }
            for v in ventas
        ]
    }), 200