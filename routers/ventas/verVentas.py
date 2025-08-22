from flask import Blueprint, jsonify
from app.models import db
from app.models.Venta import Venta
from utils.auth_utils import token_required
from flask_cors import cross_origin

ver_ventas_bp = Blueprint('ver_ventas', __name__)

@ver_ventas_bp.route('/ver', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def ver_ventas():
    try:
        ventas = Venta.query.order_by(Venta.fecha_venta.desc()).all()
        resultado = [v.to_dict() for v in ventas]
        return jsonify({'ventas': resultado}), 200
    except Exception as e:
        return jsonify({'error': 'Error al cargar las ventas', 'detalle': str(e)}), 500
    
