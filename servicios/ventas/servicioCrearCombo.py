from app.models import db
from app.models.Producto import Producto
from app.models.Venta import Venta
import random
import string

VENDEDORES_VALIDOS = ['Lauren Vanegas', 'Juan Obando']
METODOS_PAGO_VALIDOS = ['Efectivo', 'Nequi']

def generar_identificador_unico(length=8):
    caracteres = '123456789' + string.ascii_uppercase
    return ''.join(random.choices(caracteres, k=length))

def registrar_combo(nombre_combo, productos, vendido_por=None, metodo_pago=None):
    if not nombre_combo:
        return {'error': 'El nombre del combo es requerido'}, 400

    if not productos or not isinstance(productos, list):
        return {'error': 'Debe enviar la lista de productos del combo'}, 400

    if not vendido_por or vendido_por not in VENDEDORES_VALIDOS:
        return {'error': 'El campo "vendido_por" es obligatorio y debe ser válido'}, 400

    if not metodo_pago or metodo_pago not in METODOS_PAGO_VALIDOS:
        return {'error': 'El campo "metodo_pago" es obligatorio y debe ser válido'}, 400

    while True:
        identificador_combo = generar_identificador_unico()
        if not Venta.query.filter_by(identificador_unico=identificador_combo).first():
            break

    total = 0
    productos_vendidos = []

    for item in productos:
        nombre = item.get('nombre')
        cantidad = item.get('cantidad', 1)

        if not nombre or not isinstance(cantidad, int) or cantidad < 1:
            return {'error': 'Cada producto debe tener nombre y cantidad válida'}, 400

        disponibles = Producto.query.filter_by(nombre=nombre, estado='inventario').limit(cantidad).all()

        if len(disponibles) < cantidad:
            return {'error': f'Solo hay {len(disponibles)} unidades de "{nombre}" disponibles en inventario'}, 409

        for producto in disponibles:
            producto.estado = 'vendido'
            total += float(producto.precio)
            productos_vendidos.append(producto.nombre)

    nueva_venta = Venta(
        identificador_unico=identificador_combo,
        nombre_producto=nombre_combo,
        precio=round(total, 2),
        vendido_por=vendido_por,
        metodo_pago=metodo_pago,
        tipo_venta='Combo'
    )
    db.session.add(nueva_venta)

    try:
        db.session.commit()
        return {
            'mensaje': 'Combo registrado con éxito',
            'identificador_combo': identificador_combo,
            'nombre_combo': nombre_combo,
            'productos_incluidos': productos_vendidos,
            'total': round(total, 2)
        }, 201

    except Exception as e:
        db.session.rollback()
        return {'error': 'Error al registrar el combo', 'detalle': str(e)}, 500
