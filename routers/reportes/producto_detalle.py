from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from models.Producto import Producto
from models.CostoProducto import CostoProducto
from models.Venta import Venta
from utils.auth_utils import token_required
from sqlalchemy import func
from models import db

detalle_bp = Blueprint('producto_detalle', __name__)

@detalle_bp.route('/producto_detalle', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def producto_detalle():
    nombre = request.args.get('nombre')
    if not nombre:
        return jsonify({'error': 'Falta el nombre del producto'}), 400

    vendidos = db.session.query(func.count(Producto.id)).filter_by(nombre=nombre, estado='vendido').scalar()
    en_inventario = db.session.query(func.count(Producto.id)).filter_by(nombre=nombre, estado='inventario').scalar()
    total_ventas = db.session.query(func.sum(Venta.precio)).filter_by(nombre_producto=nombre).scalar() or 0

    subquery = db.session.query(
        CostoProducto.identificador_producto,
        func.max(CostoProducto.precio_compra).label('precio_compra')
    ).group_by(CostoProducto.identificador_producto).subquery()

    productos = db.session.query(Producto.identificador_unico)\
        .filter_by(nombre=nombre, estado='vendido').subquery()

    costo_total = db.session.query(func.sum(subquery.c.precio_compra))\
        .join(productos, subquery.c.identificador_producto == productos.c.identificador_unico).scalar() or 0

    ganancia = float(total_ventas - costo_total)

    return jsonify({
        'producto': nombre,
        'vendidos': vendidos,
        'en_inventario': en_inventario,
        'total_ventas': float(total_ventas),
        'costo_total': float(costo_total),
        'ganancia': ganancia
    }), 200
