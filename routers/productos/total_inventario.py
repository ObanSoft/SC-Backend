from flask import Blueprint, jsonify
from models.Producto import Producto
from sqlalchemy import func
from models.Producto import db  
from utils.auth_utils import token_required

total_inventario_bp = Blueprint('total_inventario', __name__)

@total_inventario_bp.route('/total-inventario', methods=['GET'])
@token_required
def total_precio_inventario():
    total = db.session.query(func.sum(Producto.precio)).filter(Producto.estado == 'inventario').scalar()

    return jsonify({
        'total_inventario_COP': float(total) if total else 0.0
    }), 200
