from app.models.Producto import Producto

def consultar_producto(identificador: str):
    producto = Producto.query.filter_by(identificador_unico=identificador).first()

    if not producto:
        return {'error': 'Producto no encontrado'}, 404

    return {
        'id': producto.id,
        'identificador_unico': producto.identificador_unico,
        'nombre': producto.nombre,
        'precio': str(producto.precio),
        'estado': producto.estado,
        'fecha_creacion': producto.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S') if producto.fecha_creacion else None
    }, 200
