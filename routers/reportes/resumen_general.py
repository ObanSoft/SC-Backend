from flask import Blueprint, jsonify
from flask_cors import cross_origin
from models.Producto import Producto
from models.CostoProducto import CostoProducto
from models.Venta import Venta
from utils.auth_utils import token_required
from models import db
from sqlalchemy import func

resumen_bp = Blueprint('resumen_general', __name__)

@resumen_bp.route('/resumen_general', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def resumen_general():
    
    total_vendidos = db.session.query(func.count()).select_from(Producto).filter_by(estado='vendido').scalar()
    total_inventario = db.session.query(func.count()).select_from(Producto).filter_by(estado='inventario').scalar()

    valor_inventario = db.session.query(func.sum(Producto.precio))\
    .filter(Producto.estado == 'inventario')\
    .scalar() or 0
    total_ventas = db.session.query(func.sum(Venta.precio)).scalar() or 0

    return jsonify({
        'total_productos_vendidos': total_vendidos,
        'total_en_inventario': total_inventario,
        'valor_total_inventario': float(valor_inventario),
        'total_ventas': float(total_ventas)
    }), 200
