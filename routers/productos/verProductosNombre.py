from flask import Blueprint, request, jsonify
from models.Producto import Producto
from utils.auth_utils import token_required  

buscar_nombre_bp = Blueprint('buscar_productos', __name__)

@buscar_nombre_bp.route('/buscar', methods=['GET'])
@token_required
def buscar_productos_por_nombre():
    nombre = request.args.get('nombre')

    if not nombre:
        return jsonify({'error': 'El parámetro "nombre" es requerido'}), 400

    productos = Producto.query.filter(Producto.nombre.ilike(f'%{nombre}%')).all()

    if not productos:
        return jsonify({'mensaje': 'No se encontraron productos con ese nombre'}), 404

    resultados = []
    for p in productos:
        resultados.append({
            'id': p.id,
            'identificador_unico': p.identificador_unico,
            'nombre': p.nombre,
            'precio': str(p.precio),
            'estado': p.estado,
            'fecha_creacion': p.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S') if p.fecha_creacion else None
        })

    return jsonify({
        'cantidad': len(resultados),
        'productos': resultados
    }), 200
