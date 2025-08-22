from app.models import Producto

def ver_todos_productos_servicio():
    try:
        productos = Producto.query.filter_by(estado='inventario').all()

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
        return {'error': 'No se pudieron obtener los productos', 'detalle': str(e)}, 500
