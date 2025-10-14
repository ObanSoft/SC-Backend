from .autenticacion.registro import usuarios_bp
from .autenticacion.login import login_bp

from .productos.registrarProducto import registrar_bp
from .productos.consultarProducto import consultar_bp
from .productos.eliminarProducto import eliminar_bp
from .productos.verProductosNombre import buscar_nombre_bp
from .productos.totalInventario import total_inventario_bp
from .productos.verCantidadProducto import cantidad_bp
from .productos.cambioEstado import cambio_estado_bp
from .productos.verProductos import ver_todos_bp
from .productos.disolverCombo import disolver_combo_bp

from .ventas.crearVenta import crear_venta_bp
from .ventas.verVentas import ver_ventas_bp
from .ventas.ventasPorNombre import ventas_por_nombre_bp
from .ventas.ventasPorIdentificador import venta_identificador_bp
from .ventas.margenVentas import margen_ventas_bp
from .ventas.crearVentaCombo import crear_venta_combo_bp
from .ventas.margenCombos import margen_combos_bp

from .reportes.margenPorProducto import margen_bp
from .reportes.productoDetalle import detalle_bp
from .reportes.resumenGeneral import resumen_bp
from .reportes.top5Vendidos import top5_bp
from .reportes.ventasMes import ventas_mes_bp
from .reportes.exportarVentas import exportar_excel_ventas_bp
from .reportes.exportarInventario import exportar_inventario_bp
from .reportes.exportarCombos import exportar_excel_combos_bp


def register_blueprints(app):
    blueprints = [
        (usuarios_bp, "/registro"),
        (login_bp, "/login"),
        (registrar_bp, "/productos"),
        (consultar_bp, "/productos"),
        (cantidad_bp, "/productos"),
        (eliminar_bp, "/productos"),
        (buscar_nombre_bp, "/productos"),
        (total_inventario_bp, "/productos"),
        (cambio_estado_bp, "/productos"),
        (ver_todos_bp, "/productos"),
        (disolver_combo_bp, "/productos"),
        (crear_venta_bp, "/ventas"),
        (ver_ventas_bp, "/ventas"),
        (ventas_por_nombre_bp, "/ventas"),
        (venta_identificador_bp, "/ventas"),
        (margen_ventas_bp, "/ventas"),
        (crear_venta_combo_bp, "/ventas"),
        (margen_combos_bp, "/ventas"),
        (margen_bp, "/reportes"),
        (detalle_bp, "/reportes"),
        (resumen_bp, "/reportes"),
        (top5_bp, "/reportes"),
        (ventas_mes_bp, "/reportes"),
        (exportar_excel_ventas_bp, "/reportes"),
        (exportar_inventario_bp, "/reportes"),
        (exportar_excel_combos_bp, "/reportes"),
    ]

    for bp, prefix in blueprints:
        app.register_blueprint(bp, url_prefix=prefix)
