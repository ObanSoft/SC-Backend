from app.models import Producto

def buscar_productos_por_nombre_servicio(nombre):
    if not nombre:
        return {'error': 'El parámetro "nombre" es requerido'}, 400

    try:
        productos = Producto.query.filter(
            Producto.nombre.ilike(f'%{nombre}%'),
            Producto.estado == 'Inventario'
        ).all()

        if not productos:
            return {'mensaje': 'No se encontraron productos con ese nombre'}, 404

        resultados = [
            {
                'id': p.id,
                'identificador_unico': p.identificador_unico,
                'nombre': p.nombre,
                'precio': str(p.precio),
                'estado': p.estado,
                'fecha_creacion': p.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S') if p.fecha_creacion else None
            }
            for p in productos
        ]

        return {
            'cantidad': len(resultados),
            'productos': resultados
        }, 200

    except Exception as e:
        return {'error': 'Error al buscar productos', 'detalle': str(e)}, 500
