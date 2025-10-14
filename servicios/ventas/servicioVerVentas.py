from app.models import Venta

def ver_ventas_service():
    try:
        ventas = Venta.query.order_by(Venta.fecha_venta.desc()).all()
        resultado = [v.to_dict() for v in ventas]
        return {'ventas': resultado}, 200
    except Exception as e:
        return {'error': 'Error al cargar las ventas', 'detalle': str(e)}, 500
