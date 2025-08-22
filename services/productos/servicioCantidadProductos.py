from app.models import db
from app.models.Producto import Producto
from sqlalchemy import func

def cantidad_productos_service():
    try:
        resultados = (
            db.session.query(
                Producto.nombre,
                Producto.estado,
                func.count().label('cantidad')
            )
            .filter(Producto.estado == 'inventario')
            .group_by(Producto.nombre, Producto.estado)
            .all()
        )

        productos = [
            {'nombre': nombre, 'estado': estado, 'cantidad': cantidad}
            for nombre, estado, cantidad in resultados
        ]

        return {
            'total_tipos_producto': len(productos),
            'productos': productos
        }, 200
    except Exception as e:
        return {'error': 'No se pudo obtener la cantidad de productos', 'detalle': str(e)}, 500
