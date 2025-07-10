from flask import Blueprint, jsonify
from models.Producto import Producto
from sqlalchemy import func
from models.Producto import db
from utils.auth_utils import token_required

cantidad_bp = Blueprint('cantidad_productos', __name__)

@cantidad_bp.route('/inventario/cantidad', methods=['GET'])
@token_required
def cantidad_productos_en_inventario():
    resultados = (
        db.session.query(
            Producto.nombre,
            func.count().label('cantidad')
        )
        .filter(Producto.estado == 'inventario')
        .group_by(Producto.nombre)
        .all()
    )

    productos = []
    for nombre, cantidad in resultados:
        productos.append({
            'nombre': nombre,
            'cantidad': cantidad
        })

    return jsonify({
        'total_tipos_producto': len(productos),
        'productos': productos
    }), 200
