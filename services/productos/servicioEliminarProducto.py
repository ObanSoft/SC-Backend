from app.models import db
from app.models.Producto import Producto

def eliminar_producto(identificador: str):
    producto = Producto.query.filter_by(identificador_unico=identificador).first()

    if not producto:
        return {'error': 'Producto no encontrado'}, 404

    if producto.estado != 'inventario':
        return {'error': 'Solo se pueden eliminar productos en estado de inventario'}, 403

    try:
        db.session.delete(producto)
        db.session.commit()
        return {'mensaje': f'Producto con identificador {identificador} eliminado correctamente'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': 'No se pudo eliminar el producto', 'detalle': str(e)}, 500
