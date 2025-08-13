from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from models import db, Producto, Venta
from utils.auth_utils import token_required

import random
import string

def generar_identificador_unico(length=8):
    caracteres = '123456789' + string.ascii_uppercase  
    return ''.join(random.choices(caracteres, k=length))

crear_venta_combo_bp = Blueprint('crear_venta_combo', __name__)

@crear_venta_combo_bp.route('/crearVentaCombo', methods=['POST', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def crear_venta_combo():
    data = request.get_json()

    nombre_combo = data.get('nombre_combo')  
    productos = data.get('productos')  
    vendido_por = data.get('vendido_por')
    metodo_pago = data.get('metodo_pago')
    descuento = data.get('descuento', 0)  

    while True:
        identificador_combo = generar_identificador_unico()
        existe = Venta.query.filter_by(identificador_unico=identificador_combo).first()
        if not existe:
            break

    total_sin_descuento = 0
    productos_vendidos = []

    for item in productos:
        nombre = item.get('nombre')
        cantidad = item.get('cantidad', 1)

        if not nombre or not isinstance(cantidad, int) or cantidad < 1:
            return jsonify({'error': 'Cada producto debe tener nombre y cantidad válida'}), 400

        disponibles = Producto.query.filter_by(nombre=nombre, estado='inventario').limit(cantidad).all()

        if len(disponibles) < cantidad:
            return jsonify({
                'error': f'Solo hay {len(disponibles)} unidades de "{nombre}" disponibles en inventario'
            }), 409

        for producto in disponibles:
            producto.estado = 'vendido'
            total_sin_descuento += float(producto.precio)
            productos_vendidos.append(producto.nombre)

    monto_descuento = (total_sin_descuento * descuento) / 100
    total_final = total_sin_descuento - monto_descuento

    nueva_venta = Venta(
        identificador_unico=identificador_combo,
        nombre_producto=nombre_combo,  
        precio=round(total_final, 2),
        vendido_por=vendido_por,
        metodo_pago=metodo_pago,
        tipo_venta='Combo'
    )
    db.session.add(nueva_venta)

    try:
        db.session.commit()
        return jsonify({
            'mensaje': 'Combo registrado con éxito',
            'identificador_combo': identificador_combo,
            'nombre_combo': nombre_combo,
            'productos_incluidos': productos_vendidos,
            'total_sin_descuento': round(total_sin_descuento, 2),
            'descuento_aplicado': f"{descuento}%",
            'monto_descuento': round(monto_descuento, 2),
            'total_final': round(total_final, 2)
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al registrar el combo', 'detalle': str(e)}), 500
