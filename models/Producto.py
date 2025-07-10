from models import db
from datetime import datetime
from zoneinfo import ZoneInfo

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    identificador_unico = db.Column(db.String(36), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    estado = db.Column(db.Enum('inventario', 'vendido'), nullable=False, default='inventario')
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("America/Bogota")))
