from app.models import db
from app.models.Producto import Producto
from app.models.CostoProducto import CostoProducto
from sqlalchemy import func

def obtener_margen_por_producto_servicio():
    try:
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
        return data, None
    except Exception as e:
        return None, str(e)
