from app.models import db
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy import Enum
import uuid

class Venta(db.Model):
    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)
    identificador_unico = db.Column(
        db.String(36), unique=True, nullable=False,
        default=lambda: str(uuid.uuid4())
    )
    nombre_producto = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_venta = db.Column(
        db.DateTime,
        default=lambda: datetime.now(ZoneInfo("America/Bogota"))
    )

    vendido_por = db.Column(
        Enum(
            'Lauren Vanegas',
            'Ximena Guerrero',
            'Juan Guacaneme',
            'Juan Obando',
            name='vendido_por_enum'
        ),
        nullable=True
    )

    metodo_pago = db.Column(
        Enum(
            'Efectivo',
            'Nequi',
            name='metodo_pago_enum'
        ),
        nullable=True
    )

    tipo_venta = db.Column(
        Enum(
            'Combo',
            'Individual',
            name='tipo_venta_enum'
        ),
        nullable=True
    )

    def to_dict(self):
        return {
            'id': self.id,
            'identificador_unico': self.identificador_unico,
            'nombre_producto': self.nombre_producto,
            'precio': float(self.precio),
            'fecha_venta': self.fecha_venta.strftime('%Y-%m-%d %H:%M:%S'),
            'vendido_por': self.vendido_por,
            'metodo_pago': self.metodo_pago,
            'tipo_venta': self.tipo_venta
        }
