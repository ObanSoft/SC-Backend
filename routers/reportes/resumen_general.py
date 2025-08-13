from flask import Blueprint, jsonify
from flask_cors import cross_origin
from models.Producto import Producto
from models.Venta import Venta
from utils.auth_utils import token_required
from models import db
from sqlalchemy import func

resumen_bp = Blueprint('resumen_general', __name__)

@resumen_bp.route('/resumen_general', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def resumen_general():
    try:
        # Productos en inventario
        total_inventario = db.session.query(func.count()).select_from(Producto).filter_by(estado='inventario').scalar()

        # Valor total inventario
        valor_inventario = db.session.query(func.sum(Producto.precio)).filter(Producto.estado == 'inventario').scalar() or 0

        # Total de ventas (suma precios)
        total_ventas = db.session.query(func.sum(Venta.precio)).scalar() or 0

        # Total vendidos (todos)
        total_vendidos = db.session.query(func.count()).select_from(Venta).scalar()

        # Productos individuales vendidos
        individuales_vendidos = db.session.query(func.count()).select_from(Venta).filter_by(tipo_venta='Individual').scalar()

        # Combos vendidos
        combos_vendidos = db.session.query(func.count()).select_from(Venta).filter_by(tipo_venta='Combo').scalar()

        return jsonify({
            'total_productos_vendidos': total_vendidos,
            'total_en_inventario': total_inventario,
            'valor_total_inventario': float(valor_inventario),
            'total_ventas': float(total_ventas),
            'individuales_vendidos': individuales_vendidos,
            'combos_vendidos': combos_vendidos
        }), 200

    except Exception as e:
        return jsonify({'error': 'Error al generar resumen', 'detalle': str(e)}), 500
