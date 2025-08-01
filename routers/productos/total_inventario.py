from flask import Blueprint, jsonify, request
from models.Producto import Producto
from sqlalchemy import func
from models.Producto import db
from utils.auth_utils import token_required
from flask_cors import cross_origin

total_inventario_bp = Blueprint('total_inventario', __name__)

@total_inventario_bp.route('/total-inventario', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
def total_inventario():
    if request.method == 'OPTIONS':
        return '', 200

    from utils.auth_utils import token_required

    @token_required
    def handle_get():
        total = db.session.query(func.sum(Producto.precio))\
            .filter(Producto.estado == 'inventario')\
            .scalar()

        return jsonify({
            'total_inventario_COP': round(total or 0, 2)
        }), 200

    return handle_get()


