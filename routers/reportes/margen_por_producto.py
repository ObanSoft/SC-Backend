from flask import Blueprint, jsonify
from flask_cors import cross_origin
from models.Producto import Producto
from models.CostoProducto import CostoProducto
from utils.auth_utils import token_required
from sqlalchemy import func
from models import db

margen_bp = Blueprint('margen_producto', __name__)

@margen_bp.route('/margen_por_producto', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def margen_por_producto():
    subquery = db.session.query(
        CostoProducto.identificador_producto,
        func.max(CostoProducto.precio_compra).label('precio_compra')
    ).group_by(CostoProducto.identificador_producto).subquery()

    query = db.session.query(
        Producto.nombre,
        func.count(Producto.id).label('cantidad'),
        func.sum(Producto.precio).label('venta_total'),
        func.sum(subquery.c.precio_compra).label('compra_total')
    ).join(subquery, Producto.identificador_unico == subquery.c.identificador_producto)\
     .filter(Producto.estado == 'vendido')\
     .group_by(Producto.nombre)

    data = []
    for r in query.all():
        ganancia_total = float(r.venta_total - r.compra_total)
        porcentaje = (ganancia_total / float(r.compra_total)) * 100 if r.compra_total else 0
        data.append({
            'producto': r.nombre,
            'cantidad_vendida': r.cantidad,
            'ganancia_total': ganancia_total,
            'porcentaje_ganancia': round(porcentaje, 2)
        })
    return jsonify({'margen_por_producto': data}), 200

