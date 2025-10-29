from app.models import db
from app.models.Producto import Producto
from app.models.CostoProducto import CostoProducto
from sqlalchemy import func
from datetime import datetime

def obtenerMargenTotalServicio(periodo='mes', año=None):
    try:
        año = año or datetime.now().year

        subquery = db.session.query(
            CostoProducto.identificador_producto,
            func.max(CostoProducto.precio_compra).label('precio_compra')
        ).group_by(CostoProducto.identificador_producto).subquery()

        if periodo == 'mes':
            query = db.session.query(
                func.extract('month', Producto.fecha_creacion).label('mes'),
                func.sum(Producto.precio).label('venta_total'),
                func.sum(subquery.c.precio_compra).label('compra_total')
            ).join(subquery, Producto.identificador_unico == subquery.c.identificador_producto)\
             .filter(Producto.estado == 'vendido')\
             .filter(func.extract('year', Producto.fecha_creacion) == año)\
             .group_by(func.extract('month', Producto.fecha_creacion))\
             .order_by(func.extract('month', Producto.fecha_creacion))
        else:  
            query = db.session.query(
                func.extract('year', Producto.fecha_creacion).label('año'),
                func.sum(Producto.precio).label('venta_total'),
                func.sum(subquery.c.precio_compra).label('compra_total')
            ).join(subquery, Producto.identificador_unico == subquery.c.identificador_producto)\
             .filter(Producto.estado == 'vendido')\
             .group_by(func.extract('year', Producto.fecha_creacion))\
             .order_by(func.extract('year', Producto.fecha_creacion))

        data = []
        for r in query.all():
            venta_total = float(r.venta_total or 0)
            compra_total = float(r.compra_total or 0)
            ganancia_total = venta_total - compra_total
            porcentaje = (ganancia_total / compra_total) * 100 if compra_total else 0

            if periodo == 'mes':
                data.append({
                    'mes': int(r.mes),
                    'venta_total': round(venta_total, 2),
                    'ganancia_total': round(ganancia_total, 2),
                    'porcentaje_ganancia': round(porcentaje, 2)
                })
            else:
                data.append({
                    'año': int(r.año),
                    'venta_total': round(venta_total, 2),
                    'ganancia_total': round(ganancia_total, 2),
                    'porcentaje_ganancia': round(porcentaje, 2)
                })

        return data, None
    except Exception as e:
        return None, str(e)
