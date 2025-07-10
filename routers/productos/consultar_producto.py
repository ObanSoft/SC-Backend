from flask import Blueprint, jsonify
from models.Producto import Producto
from utils.auth_utils import token_required  

consultar_bp = Blueprint('consultar_producto', __name__)

@consultar_bp.route('/consultar_producto/<identificador>', methods=['GET'])
@token_required  
def consultar_producto(identificador):
    producto = Producto.query.filter_by(identificador_unico=identificador).first()

    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404

    return jsonify({
        'id': producto.id,
        'identificador_unico': producto.identificador_unico,
        'nombre': producto.nombre,
        'precio': str(producto.precio),
        'estado': producto.estado,
        'fecha_creacion': producto.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S') if producto.fecha_creacion else None
    }), 200
