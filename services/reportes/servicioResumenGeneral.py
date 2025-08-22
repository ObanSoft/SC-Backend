from app.models import db
from app.models.Producto import Producto
from app.models.Venta import Venta
from sqlalchemy import func

def obtener_resumen_general_servicio():
    try:
        total_inventario = db.session.query(func.count()).select_from(Producto).filter_by(estado='inventario').scalar()

        valor_inventario = db.session.query(func.sum(Producto.precio)).filter(Producto.estado == 'inventario').scalar() or 0

        total_ventas = db.session.query(func.sum(Venta.precio)).scalar() or 0

        total_vendidos = db.session.query(func.count()).select_from(Venta).scalar()

        individuales_vendidos = db.session.query(func.count()).select_from(Venta).filter_by(tipo_venta='Individual').scalar()

        combos_vendidos = db.session.query(func.count()).select_from(Venta).filter_by(tipo_venta='Combo').scalar()

        resultado = {
            'total_productos_vendidos': total_vendidos,
            'total_en_inventario': total_inventario,
            'valor_total_inventario': float(valor_inventario),
            'total_ventas': float(total_ventas),
            'individuales_vendidos': individuales_vendidos,
            'combos_vendidos': combos_vendidos
        }

        return resultado, None

    except Exception as e:
        return None, str(e)
