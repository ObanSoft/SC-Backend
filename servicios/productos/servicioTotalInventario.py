from sqlalchemy import func
from app.models import db
from app.models.Producto import Producto

def total_inventario_service():
    try:
        total = db.session.query(func.sum(Producto.precio))\
            .filter(Producto.estado == 'inventario')\
            .scalar()
        return {'total_inventario_COP': round(total or 0, 2)}, 200
    except Exception as e:
        return {'error': 'No se pudo calcular el total del inventario', 'detalle': str(e)}, 500
