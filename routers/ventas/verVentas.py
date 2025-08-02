from flask import Blueprint, jsonify
from models.Venta import Venta
from utils.auth_utils import token_required
from flask_cors import cross_origin

ver_ventas_bp = Blueprint('ver_ventas', __name__)

@ver_ventas_bp.route('/ver', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def ver_ventas():
    try:
        ventas = Venta.query.order_by(Venta.fecha_venta.desc()).all()
        resultado = [
            {
                'id': v.id,
                'identificador_unico': v.identificador_unico,
                'nombre_producto': v.nombre_producto,
                'precio': float(v.precio),
                'fecha_venta': v.fecha_venta.strftime('%Y-%m-%d %H:%M:%S')
            }
            for v in ventas
        ]
        return jsonify({'ventas': resultado}), 200
    except Exception as e:
        return jsonify({'error': 'Error al cargar las ventas', 'detalle': str(e)}), 500
