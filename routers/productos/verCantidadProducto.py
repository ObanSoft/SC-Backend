from flask import Blueprint, jsonify, request
from models.Producto import Producto
from sqlalchemy import func
from models.Producto import db
from utils.auth_utils import token_required
from flask_cors import cross_origin

cantidad_bp = Blueprint('cantidad_productos', __name__)

@cantidad_bp.route('/inventario/cantidad', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
def cantidad_productos_en_inventario():
    if request.method == 'OPTIONS':
        return '', 200

    from utils.auth_utils import token_required

    @token_required
    def handle_get():
        resultados = (
            db.session.query(
                Producto.nombre,
                func.count().label('cantidad')
            )
            .filter(Producto.estado == 'inventario')
            .group_by(Producto.nombre)
            .all()
        )

        productos = [
            {'nombre': nombre, 'cantidad': cantidad}
            for nombre, cantidad in resultados
        ]

        return jsonify({
            'total_tipos_producto': len(productos),
            'productos': productos
        }), 200

    return handle_get()

