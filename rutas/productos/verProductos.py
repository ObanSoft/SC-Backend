from flask import Blueprint, jsonify
from utils.auth_utils import token_required
from servicios.productos.servicioVerProductos import ver_todos_productos_servicio

ver_todos_bp = Blueprint('verProductos', __name__)

@ver_todos_bp.route('/verProductos', methods=['GET'])
@token_required
def ver_todos_los_productos():
    response, status = ver_todos_productos_servicio()
    return jsonify(response), status
