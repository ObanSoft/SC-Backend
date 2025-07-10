from flask import Blueprint, request, jsonify
from models.Producto import db, Producto
from sqlalchemy.exc import IntegrityError
from utils.auth_utils import token_required
import random
import string


registrar_bp = Blueprint('registrar_producto', __name__)

def generar_identificador():
    import random
    import string
    numeros = ''.join(random.choices('123456789', k=5))
    letras = ''.join(random.choices(string.ascii_uppercase, k=5))
    lista = list(numeros + letras)
    random.shuffle(lista)
    return ''.join(lista)

@registrar_bp.route('/registrar_producto', methods=['POST'])
@token_required
def registrar_producto():
    data = request.get_json()
    nombre = data.get('nombre')
    precio = data.get('precio')
    cantidad = data.get('cantidad', 1)

    if not nombre or not precio or cantidad < 1:
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
            precio=precio,
            estado="inventario"
        )
        db.session.add(nuevo_producto)
        productos_creados.append(nuevo_producto)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Error de integridad, puede que el identificador ya exista'}), 500

    return jsonify({
        'mensaje': f'{cantidad} producto(s) registrado(s)',
        'productos': [p.identificador_unico for p in productos_creados]
    }), 201