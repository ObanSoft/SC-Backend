from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from utils.auth_utils import token_required
from servicios.ventas.servicioVerVentas import ver_ventas_service

ver_ventas_bp = Blueprint('verVentas', __name__)

@ver_ventas_bp.route('/verVentas', methods=['GET'])
@token_required
def ver_ventas():
    response, status = ver_ventas_service()
    return jsonify(response), status
