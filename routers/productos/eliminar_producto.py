from flask import Blueprint, jsonify, request
from models.Producto import Producto
from models.Producto import db  
from utils.auth_utils import token_required
from flask_cors import cross_origin

eliminar_bp = Blueprint('eliminar_producto', __name__)

@eliminar_bp.route('/eliminar_producto/<identificador>', methods=['DELETE', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
def eliminar_producto(identificador):
    if request.method == 'OPTIONS':
        return '', 200

    @token_required
    def handle_delete():
        producto = Producto.query.filter_by(identificador_unico=identificador).first()

        if not producto:
            return jsonify({'error': 'Producto no encontrado'}), 404

        if producto.estado != 'inventario':
            return jsonify({'error': 'Solo se pueden eliminar productos en estado de inventario'}), 403

        db.session.delete(producto)
        db.session.commit()

        return jsonify({'mensaje': f'Producto con identificador {identificador} eliminado correctamente'}), 200

    return handle_delete()
