from flask import Blueprint, jsonify
from models.Venta import Venta
from utils.auth_utils import token_required

ventas_por_nombre_bp = Blueprint('ventas_por_nombre', __name__)

@ventas_por_nombre_bp.route('/producto/<nombre_producto>', methods=['GET'])
@token_required
def obtener_ventas_por_nombre(nombre_producto):
    ventas = Venta.query.filter_by(nombre_producto=nombre_producto).all()

    if not ventas:
        return jsonify({'error': f'No se encontraron ventas para \"{nombre_producto}\"'}), 404

    return jsonify({
        'nombre_producto': nombre_producto,
        'total_ventas': len(ventas),
        'ventas': [
            {
                'identificador_unico': v.identificador_unico,
                'precio': float(v.precio),
                'fecha_venta': v.fecha_venta.strftime('%Y-%m-%d %H:%M:%S')
            }
            for v in ventas
        ]
    }), 200
