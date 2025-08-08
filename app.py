from flask import Flask
from flask_cors import CORS
from config import Config
from models import db


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

app.config.from_object(Config)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{app.config['DB_USER']}:{app.config['DB_PASSWORD']}"
    f"@{app.config['DB_HOST']}/{app.config['DB_NAME']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from routers.auth.registro import usuarios_bp
from routers.auth.login import login_bp

from routers.productos.registrar_producto import registrar_bp
from routers.productos.consultar_producto import consultar_bp
from routers.productos.eliminar_producto import eliminar_bp
from routers.productos.verProductosNombre import buscar_nombre_bp
from routers.productos.total_inventario import total_inventario_bp
from routers.productos.verCantidadProducto import cantidad_bp
from routers.productos.cambioEstado import cambio_estado_bp
from routers.productos.verProductos import ver_todos_bp

from routers.ventas.crearVenta import crear_venta_bp
from routers.ventas.verVentas import ver_ventas_bp         
from routers.ventas.ventaIdentificador import venta_identificador_bp  
from routers.ventas.ventasProductos import ventas_por_nombre_bp
from routers.ventas.margenVentas import margen_ventas_bp

from routers.reportes.margen_por_producto import margen_bp
from routers.reportes.producto_detalle import detalle_bp
from routers.reportes.resumen_general import resumen_bp
from routers.reportes.top5_mas_vendidos import top5_bp
from routers.reportes.ventas_por_mes import ventas_mes_bp
from routers.reportes.exportar_ventas import exportar_excel_ventas_bp
from routers.reportes.exportar_inventario import exportar_inventario_bp

app.register_blueprint(usuarios_bp, url_prefix="/registro")
app.register_blueprint(login_bp, url_prefix="/login")

app.register_blueprint(registrar_bp, url_prefix="/productos")
app.register_blueprint(consultar_bp, url_prefix="/productos")
app.register_blueprint(cantidad_bp, url_prefix="/productos")
app.register_blueprint(eliminar_bp, url_prefix="/productos")
app.register_blueprint(buscar_nombre_bp, url_prefix="/productos")
app.register_blueprint(total_inventario_bp, url_prefix="/productos")
app.register_blueprint(cambio_estado_bp, url_prefix="/productos")
app.register_blueprint(ver_todos_bp, url_prefix="/productos")

app.register_blueprint(crear_venta_bp, url_prefix="/ventas")
app.register_blueprint(ver_ventas_bp, url_prefix="/ventas")              
app.register_blueprint(venta_identificador_bp, url_prefix="/ventas")     
app.register_blueprint(ventas_por_nombre_bp, url_prefix="/ventas")
app.register_blueprint(margen_ventas_bp, url_prefix="/ventas")

app.register_blueprint(margen_bp, url_prefix="/reportes")
app.register_blueprint(detalle_bp, url_prefix="/reportes")
app.register_blueprint(resumen_bp, url_prefix="/reportes")
app.register_blueprint(top5_bp, url_prefix="/reportes")
app.register_blueprint(ventas_mes_bp, url_prefix="/reportes")
app.register_blueprint(exportar_excel_ventas_bp, url_prefix="/reportes")
app.register_blueprint(exportar_inventario_bp, url_prefix="/reportes")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
