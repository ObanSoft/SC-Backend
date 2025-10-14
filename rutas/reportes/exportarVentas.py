from flask import Blueprint, send_file, jsonify, request
from utils.auth_utils import token_required
from servicios.reportes.servicioExportarVentas import exportar_ventas_servicio

exportar_excel_ventas_bp = Blueprint('exportarExcelVentas', __name__)

@exportar_excel_ventas_bp.route('/exportarExcelVentas', methods=['GET'])
@token_required
def exportar_excel_ventas():

    output, error = exportar_ventas_servicio()
    if error:
        return jsonify({'error': 'Error al generar el Excel', 'detalle': error}), 500

    return send_file(
        output,
        as_attachment=True,
        download_name='reporte_ventas_individuales.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
