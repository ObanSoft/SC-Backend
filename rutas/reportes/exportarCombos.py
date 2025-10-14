from flask import Blueprint, send_file, jsonify, request
from utils.auth_utils import token_required
from servicios.reportes.servicioExportarCombos import exportar_combos_servicio

exportar_excel_combos_bp = Blueprint('exportarExcelCombos', __name__)

@exportar_excel_combos_bp.route('/exportarExcelCombos', methods=['GET'])
@token_required
def exportar_excel_combos():
    output, error = exportar_combos_servicio()
    if error:
        return jsonify({'error': 'Error al generar el Excel', 'detalle': error}), 500

    return send_file(
        output,
        as_attachment=True,
        download_name='reporte_combos.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
