from app.models import db
from app.models.Venta import Venta
from sqlalchemy import extract, func
from calendar import month_name

def obtener_ventas_por_mes():
    try:
        resultados = Venta.query.with_entities(
            extract('year', Venta.fecha_venta).label('anio'),
            extract('month', Venta.fecha_venta).label('mes'),
            func.count().label('cantidad'),
            func.sum(Venta.precio).label('total')
        ).group_by('anio', 'mes').order_by('anio', 'mes').all()

        data = [
            {
                'anio': int(r.anio),
                'mes': month_name[int(r.mes)],
                'cantidad_vendida': r.cantidad,
                'total_ventas': float(r.total)
            } for r in resultados
        ]
        return data, 200
    except Exception as e:
        return {'error': 'No se pudieron obtener las ventas por mes', 'detalle': str(e)}, 500
