from flask import Blueprint, jsonify
from models import db
from models.Producto import Producto
from models.Venta import Venta
from utils.auth_utils import token_required

cambio_estado_bp = Blueprint('cambio_estado', __name__)

@cambio_estado_bp.route('/cambiar_estado/<identificador_unico>', methods=['PUT'])
@token_required
def cambiar_estado_producto(identificador_unico):
    producto = Producto.query.filter_by(identificador_unico=identificador_unico).first()
    venta = Venta.query.filter_by(identificador_unico=identificador_unico).first()

    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404

    if producto.estado != 'vendido':
        return jsonify({'mensaje': 'Este producto ya está en inventario. No se requiere revertir venta.'}), 200

    if not venta:
        return jsonify({'error': 'No se encontró una venta asociada al producto'}), 404

    try:
        db.session.delete(venta)
        producto.estado = 'inventario'
        db.session.commit()

        return jsonify({
            'mensaje': f'El producto "{producto.nombre}" ha sido devuelto a inventario y la venta eliminada',
            'identificador_unico': identificador_unico
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'No se pudo revertir la venta', 'detalle': str(e)}), 500
