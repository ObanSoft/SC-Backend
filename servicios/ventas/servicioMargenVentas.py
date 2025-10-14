from app.models import db
from app.models.Venta import Venta
from sqlalchemy import func

def calcular_margen_ventas():
    total_ventas = db.session.query(func.sum(Venta.precio))\
        .filter(Venta.tipo_venta == 'Individual')\
        .scalar() or 0.0

    return {
        'mensaje': 'Margen total de ventas',
        'total_ventas_cop': float(total_ventas)
    }, 200
