from flask import Blueprint, request, jsonify
from models.Producto import db, Producto
from models.CostoProducto import CostoProducto
from sqlalchemy.exc import IntegrityError
from utils.auth_utils import token_required
from flask_cors import cross_origin
import random
import string

registrar_bp = Blueprint('registrar_producto', __name__)

def generar_identificador():
    numeros = ''.join(random.choices('123456789', k=5))
    letras = ''.join(random.choices(string.ascii_uppercase, k=5))
    lista = list(numeros + letras)
    random.shuffle(lista)
    return ''.join(lista)

@registrar_bp.route('/registrar_producto', methods=['POST', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
def registrar_producto():
    if request.method == 'OPTIONS':
        return '', 200

    @token_required
    def handle_post():
        data = request.get_json()
        nombre = data.get('nombre')
        precio_venta = data.get('precio_venta')  
        precio_compra = data.get('precio_compra')  
        cantidad = data.get('cantidad', 1)

        if not nombre or not precio_venta or not precio_compra or cantidad < 1:
            return jsonify({'error': 'Datos incompletos o cantidad inválida'}), 400

        productos_creados = []
        for _ in range(cantidad):
            for _ in range(10):
                identificador = generar_identificador()
                existe = Producto.query.filter_by(identificador_unico=identificador).first()
                if not existe:
                    break
            else:
                return jsonify({'error': 'No se pudo generar un identificador único'}), 500

            nuevo_producto = Producto(
                identificador_unico=identificador,
                nombre=nombre,
                precio=precio_venta,
                estado="inventario"
            )
            db.session.add(nuevo_producto)
            productos_creados.append(nuevo_producto)

            nuevo_costo = CostoProducto(
                identificador_producto=identificador,
                precio_compra=precio_compra
            )
            db.session.add(nuevo_costo)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Error de integridad'}), 500

        return jsonify({
            'mensaje': f'{cantidad} producto(s) registrado(s)',
            'productos': [p.identificador_unico for p in productos_creados]
        }), 201

    return handle_post()
