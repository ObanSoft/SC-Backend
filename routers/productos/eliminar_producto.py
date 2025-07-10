from flask import Blueprint, jsonify
from models.Producto import Producto
from models.Producto import db  
from utils.auth_utils import token_required

eliminar_bp = Blueprint('eliminar_producto', __name__)

@eliminar_bp.route('/eliminar_producto/<identificador>', methods=['DELETE'])
@token_required  
def eliminar_producto(identificador):
    producto = Producto.query.filter_by(identificador_unico=identificador).first()

    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404

    if producto.estado != 'inventario':
        return jsonify({'error': 'Solo se pueden eliminar productos en estado de inventario'}), 403

    db.session.delete(producto)
    db.session.commit()

    return jsonify({'mensaje': f'Producto con identificador {identificador} eliminado correctamente'}), 200
