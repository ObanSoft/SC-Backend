from app.models import db
from app.models.Producto import Producto
from app.models.Venta import Venta

def disolver_combo(identificador_combo: str):
    if not identificador_combo:
        return {'error': 'El identificador del combo es obligatorio'}, 400

    venta = Venta.query.filter_by(identificador_unico=identificador_combo, tipo_venta='Combo').first()
    if not venta:
        return {'error': 'No se encontró la venta combo con ese identificador'}, 404

    productos_vendidos = Producto.query.filter_by(estado='vendido').all()
    if not productos_vendidos:
        return {'error': 'No se encontraron productos vendidos para este combo'}, 404

    for producto in productos_vendidos:
        producto.estado = 'inventario'

    try:
        db.session.delete(venta)
        db.session.commit()
        return {
            'mensaje': f'Combo con ID {identificador_combo} disuelto y productos devueltos al inventario',
            'productos_restaurados': [p.nombre for p in productos_vendidos]
        }, 200
    except Exception as e:
        db.session.rollback()
        return {'error': 'Error al disolver el combo', 'detalle': str(e)}, 500
