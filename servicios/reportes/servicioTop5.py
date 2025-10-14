from app.models import db
from app.models.Venta import Venta
from sqlalchemy import func

def obtener_top5_mas_vendidos():
    try:
        resultados = Venta.query.with_entities(
            Venta.nombre_producto,
            func.count(Venta.id).label('cantidad')
        ).group_by(Venta.nombre_producto)\
         .order_by(func.count(Venta.id).desc())\
         .limit(5).all()

        data = [{'producto': r.nombre_producto, 'cantidad_vendida': r.cantidad} for r in resultados]
        return data, 200
    except Exception as e:
        return {'error': 'No se pudo obtener el top 5 de productos', 'detalle': str(e)}, 500
