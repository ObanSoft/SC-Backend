from flask import Blueprint, jsonify
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.productos.servicioTotalInventario import total_inventario_service

total_inventario_bp = Blueprint('total_inventario', __name__)

@total_inventario_bp.route('/total-inventario', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def total_inventario():
    if request.method == 'OPTIONS':
        return '', 200

    response, status = total_inventario_service()
    return jsonify(response), status
