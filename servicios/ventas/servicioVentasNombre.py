from app.models import db
from app.models.Venta import Venta

def obtener_ventas_por_nombre_service(nombre_producto):
    nombre_limpio = nombre_producto.strip()
    ventas = Venta.query.filter_by(nombre_producto=nombre_limpio).all()

    if not ventas:
        return {'error': f'No se encontraron ventas para "{nombre_limpio}"'}, 404

    ventas_lista = [
        {
            'identificador_unico': v.identificador_unico,
            'precio': float(v.precio),
            'fecha_venta': v.fecha_venta.strftime('%Y-%m-%d %H:%M:%S') if v.fecha_venta else None,
            'tipo_venta': v.tipo_venta,
            'vendido_por': v.vendido_por
        }
        for v in ventas
    ]

    return {
        'nombre_producto': nombre_limpio,
        'total_ventas': len(ventas_lista),
        'ventas': ventas_lista
    }, 200
