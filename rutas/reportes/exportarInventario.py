from flask import Blueprint, send_file, jsonify, request
from utils.auth_utils import token_required
from servicios.reportes.servicioExportarInventario import exportar_inventario_servicio

exportar_inventario_bp = Blueprint('exportarExcelInventario', __name__)

@exportar_inventario_bp.route('/exportarExcelInventario', methods=['GET'])
@token_required
def descargar_excel_inventario():
    output, error = exportar_inventario_servicio()
    if error:
        return jsonify({'error': 'Error al generar el Excel', 'detalle': error}), 500

    return send_file(
        output,
        as_attachment=True,
        download_name='reporte_inventario.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
