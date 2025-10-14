from app.models import db
from app.models.Producto import Producto
from app.models.Venta import Venta

VENDEDORES_VALIDOS = ['Lauren Vanegas','Juan Obando']
METODOS_PAGO_VALIDOS = ['Efectivo', 'Nequi']

def registrar_ventas(nombre_producto, cantidad=1, vendido_por=None, metodo_pago=None):
    if not nombre_producto:
        return {'error': 'El nombre del producto es requerido'}, 400

    if not isinstance(cantidad, int) or cantidad < 1:
        return {'error': 'La cantidad debe ser un número entero positivo'}, 400

    if not vendido_por or vendido_por not in VENDEDORES_VALIDOS:
        return {'error': 'El campo "vendido_por" es obligatorio y debe ser válido'}, 400

    if not metodo_pago or metodo_pago not in METODOS_PAGO_VALIDOS:
        return {'error': 'El campo "metodo_pago" es obligatorio y debe ser válido'}, 400

    productos_disponibles = Producto.query.filter_by(nombre=nombre_producto, estado='inventario').limit(cantidad).all()

    if len(productos_disponibles) < cantidad:
        return {
            'error': f'Solo hay {len(productos_disponibles)} unidades de "{nombre_producto}" disponibles en inventario'
        }, 409

    ventas_realizadas = []

    for producto in productos_disponibles:
        venta_existente = Venta.query.filter_by(identificador_unico=producto.identificador_unico).first()
        if venta_existente:
            continue  

        nueva_venta = Venta(
            identificador_unico=producto.identificador_unico,
            nombre_producto=producto.nombre,
            precio=producto.precio,
            vendido_por=vendido_por,
            metodo_pago=metodo_pago,
            tipo_venta='Individual',
        )
        db.session.add(nueva_venta)
        producto.estado = 'vendido'
        ventas_realizadas.append({
            'identificador_unico': producto.identificador_unico,
            'nombre_producto': producto.nombre,
            'precio': float(producto.precio),
            'vendido_por': vendido_por,
            'metodo_pago': metodo_pago
        })

    if not ventas_realizadas:
        return {'error': 'No se pudo registrar ninguna venta. Los productos ya están vendidos.'}, 409

    try:
        db.session.commit()
        return {
            'mensaje': f'{len(ventas_realizadas)} venta(s) registrada(s) exitosamente',
            'ventas': ventas_realizadas
        }, 201
    except Exception as e:
        db.session.rollback()
        return {'error': 'Error al registrar la(s) venta(s)', 'detalle': str(e)}, 500
