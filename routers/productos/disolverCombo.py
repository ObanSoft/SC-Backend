from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from models import db, Producto, Venta
from utils.auth_utils import token_required



disolver_combo_bp = Blueprint('disolver_combo', __name__)

@disolver_combo_bp.route('/disolverCombo', methods=['POST', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def disolver_combo():
    data = request.get_json()
    identificador_combo = data.get('identificador_combo')

    if not identificador_combo:
        return jsonify({'error': 'El identificador del combo es obligatorio'}), 400


    venta = Venta.query.filter_by(identificador_unico=identificador_combo, tipo_venta='Combo').first()
    if not venta:
        return jsonify({'error': 'No se encontró la venta combo con ese identificador'}), 404
    productos_vendidos = Producto.query.filter_by(estado='vendido').all()

    if not productos_vendidos:
        return jsonify({'error': 'No se encontraron productos vendidos para este combo'}), 404

    for producto in productos_vendidos:
        producto.estado = 'inventario'

    try:
        db.session.delete(venta)
        db.session.commit()
        return jsonify({
            'mensaje': f'Combo con ID {identificador_combo} disuelto y productos devueltos al inventario',
            'productos_restaurados': [p.nombre for p in productos_vendidos]
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al disolver el combo', 'detalle': str(e)}), 500