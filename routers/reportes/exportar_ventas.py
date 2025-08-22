from flask import Blueprint, send_file, jsonify, request
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.reportes.servicioExportarVentas import exportar_ventas_servicio

exportar_excel_ventas_bp = Blueprint('exportar_excel_ventas', __name__)

@exportar_excel_ventas_bp.route('/exportar_ventas', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def exportar_excel_ventas():
    if request.method == 'OPTIONS':
        return '', 200

    output, error = exportar_ventas_servicio()
    if error:
        return jsonify({'error': 'Error al generar el Excel', 'detalle': error}), 500

    return send_file(
        output,
        as_attachment=True,
        download_name='reporte_ventas_individuales.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
