from flask import Blueprint, request, jsonify
from models import db
from models.Producto import Producto
from models.Venta import Venta
from utils.auth_utils import token_required
from flask_cors import cross_origin

crear_venta_bp = Blueprint('crear_venta', __name__)

@crear_venta_bp.route('/crearVenta', methods=['POST' , 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def crear_venta():
    data = request.get_json()
    nombre_producto = data.get('nombre_producto')
    cantidad = data.get('cantidad', 1)

    if not nombre_producto:
        return jsonify({'error': 'El nombre del producto es requerido'}), 400

    if not isinstance(cantidad, int) or cantidad < 1:
        return jsonify({'error': 'La cantidad debe ser un número entero positivo'}), 400

    productos_disponibles = Producto.query.filter_by(nombre=nombre_producto, estado='inventario').limit(cantidad).all()

    if len(productos_disponibles) < cantidad:
        return jsonify({
            'error': f'Solo hay {len(productos_disponibles)} unidades de "{nombre_producto}" disponibles en inventario'
        }), 409

    ventas_realizadas = []

    for producto in productos_disponibles:
        if producto.estado == 'vendido':
            continue

        venta_existente = Venta.query.filter_by(identificador_unico=producto.identificador_unico).first()
        if venta_existente:
            continue  

        nueva_venta = Venta(
            identificador_unico=producto.identificador_unico,
            nombre_producto=producto.nombre,
            precio=producto.precio
        )
        db.session.add(nueva_venta)
        producto.estado = 'vendido'
        ventas_realizadas.append({
            'identificador_unico': producto.identificador_unico,
            'nombre_producto': producto.nombre,
            'precio': float(producto.precio)
        })

    if not ventas_realizadas:
        return jsonify({'error': 'No se pudo registrar ninguna venta. Los productos ya están vendidos.'}), 409

    try:
        db.session.commit()
        return jsonify({
            'mensaje': f'{len(ventas_realizadas)} venta(s) registrada(s) exitosamente',
            'ventas': ventas_realizadas
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al registrar la(s) venta(s)', 'detalle': str(e)}), 500
