from flask import Blueprint, jsonify
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.productos.servicioConsultarProducto import consultar_producto as consultar_producto_service

consultar_bp = Blueprint('consultar_producto', __name__)

@consultar_bp.route('/consultar_producto/<identificador>', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def consultar_producto(identificador):
    response, status = consultar_producto_service(identificador)
    return jsonify(response), status
