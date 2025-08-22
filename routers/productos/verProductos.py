from flask import Blueprint, jsonify
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.productos.servicioVerProductos import ver_todos_productos_servicio

ver_todos_bp = Blueprint('ver_todos', __name__)

@ver_todos_bp.route('/ver', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def ver_todos_los_productos():
    response, status = ver_todos_productos_servicio()
    return jsonify(response), status
