from app.models import db
from app.models.Venta import Venta
from sqlalchemy import func

def calcular_margen_combos():
    total_combos = db.session.query(func.sum(Venta.precio))\
        .filter(Venta.tipo_venta == 'Combo')\
        .scalar() or 0.0

    return {
        'mensaje': 'Margen total de combos',
        'total_combos_cop': float(total_combos)
    }, 200
