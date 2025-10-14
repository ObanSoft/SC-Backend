from app.models import db
from app.models.Venta import Venta

def obtener_venta_por_identificador(identificador_unico):
    venta = Venta.query.filter_by(identificador_unico=identificador_unico, tipo_venta='Individual').first()

    if not venta:
        return {
            'error': f'No se encontró ninguna venta individual registrada con el identificador "{identificador_unico}"'
        }, 404

    return {
        'identificador_unico': venta.identificador_unico,
        'nombre_producto': venta.nombre_producto,
        'precio': float(venta.precio),
        'fecha_venta': venta.fecha_venta.strftime('%Y-%m-%d %H:%M:%S') if venta.fecha_venta else None,
        'tipo_venta': venta.tipo_venta,
        'vendido_por': venta.vendido_por,
        'metodo_pago': venta.metodo_pago
    }, 200
