from app.models import db
from datetime import datetime

class CostoProducto(db.Model):
    __tablename__ = 'costos_producto'

    id = db.Column(db.Integer, primary_key=True)
    identificador_producto = db.Column(db.String(36), nullable=False)  
    precio_compra = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
