from flask import Blueprint, jsonify
from models.Producto import Producto
from utils.auth_utils import token_required

ver_todos_bp = Blueprint('ver_todos', __name__)

@ver_todos_bp.route('/ver', methods=['GET'])
@token_required
def ver_todos_los_productos():
    productos = Producto.query.filter_by(estado='inventario').all()  

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
