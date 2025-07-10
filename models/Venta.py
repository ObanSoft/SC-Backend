from models import db
from datetime import datetime
from zoneinfo import ZoneInfo
import uuid

class Venta(db.Model):
    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)
    identificador_unico = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    nombre_producto = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_venta = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("America/Bogota")))
