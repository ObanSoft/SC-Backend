from flask import Blueprint, send_file, jsonify, request
from flask_cors import cross_origin
from utils.auth_utils import token_required
from services.reportes.servicioExportarInventario import exportar_inventario_servicio

exportar_inventario_bp = Blueprint('exportar_inventario', __name__)

@exportar_inventario_bp.route('/exportar_inventario', methods=['GET', 'OPTIONS'], strict_slashes=False)
@cross_origin(origin='http://localhost:3000', supports_credentials=True)
@token_required
def descargar_excel_inventario():
    if request.method == 'OPTIONS':
        return '', 200

    output, error = exportar_inventario_servicio()
    if error:
        return jsonify({'error': 'Error al generar el Excel', 'detalle': error}), 500

    return send_file(
        output,
        as_attachment=True,
        download_name='reporte_inventario.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
