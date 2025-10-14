from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from utils.auth_utils import token_required
from servicios.ventas.servicioVentaIdentificador import obtener_venta_por_identificador

venta_identificador_bp = Blueprint('ventaPorIdentificador', __name__)

@venta_identificador_bp.route('ventaPorIdentificador/<identificador_unico>', methods=['GET'])
@token_required
def venta_por_id(identificador_unico):
    response, status = obtener_venta_por_identificador(identificador_unico)
    return jsonify(response), status
