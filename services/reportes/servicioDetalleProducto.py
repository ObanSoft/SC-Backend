from app.models import db
from app.models.Producto import Producto
from app.models.CostoProducto import CostoProducto
from app.models.Venta import Venta
from sqlalchemy import func

def obtener_detalle_producto_servicio(nombre):
    if not nombre:
        return None, 'Falta el nombre del producto'
    
    try:
        vendidos = db.session.query(func.count(Producto.id))\
            .filter_by(nombre=nombre, estado='vendido').scalar()
        en_inventario = db.session.query(func.count(Producto.id))\
            .filter_by(nombre=nombre, estado='inventario').scalar()
        total_ventas = db.session.query(func.sum(Venta.precio))\
            .filter_by(nombre_producto=nombre).scalar() or 0

        subquery = db.session.query(
            CostoProducto.identificador_producto,
            func.max(CostoProducto.precio_compra).label('precio_compra')
        ).group_by(CostoProducto.identificador_producto).subquery()

        productos_vendidos = db.session.query(Producto.identificador_unico)\
            .filter_by(nombre=nombre, estado='vendido').subquery()

        costo_total = db.session.query(func.sum(subquery.c.precio_compra))\
            .join(productos_vendidos, subquery.c.identificador_producto == productos_vendidos.c.identificador_unico)\
            .scalar() or 0

        ganancia = float(total_ventas - costo_total)

        resultado = {
            'producto': nombre,
            'vendidos': vendidos,
            'en_inventario': en_inventario,
            'total_ventas': float(total_ventas),
            'costo_total': float(costo_total),
            'ganancia': ganancia
        }

        return resultado, None
    except Exception as e:
        return None, str(e)
