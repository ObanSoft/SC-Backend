from flask import Blueprint, jsonify
from models.Venta import Venta
from utils.auth_utils import token_required

venta_identificador_bp = Blueprint('venta_identificador', __name__)

@venta_identificador_bp.route('/<identificador_unico>', methods=['GET'])
@token_required
def obtener_venta_por_id(identificador_unico):
    try:
        venta = Venta.query.filter_by(identificador_unico=identificador_unico).first()

        if not venta:
            return jsonify({'error': f'No se encontró ninguna venta registrada con el identificador "{identificador_unico}"'}), 404

        return jsonify({
            'identificador_unico': venta.identificador_unico,
            'nombre_producto': venta.nombre_producto,
            'precio': float(venta.precio),
            'fecha_venta': venta.fecha_venta.strftime('%Y-%m-%d %H:%M:%S')
        }), 200

    except Exception as e:
        return jsonify({'error': 'Error al consultar la venta', 'detalle': str(e)}), 500
