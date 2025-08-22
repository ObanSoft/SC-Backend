from flask import Blueprint, jsonify
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.productos.servicioCantidadProductos import cantidad_productos_service

cantidad_bp = Blueprint('cantidad_productos', __name__)

@cantidad_bp.route('/inventario/cantidad', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def cantidad_productos_en_inventario():
    if request.method == 'OPTIONS':
        return '', 200

    response, status = cantidad_productos_service()
    return jsonify(response), status
