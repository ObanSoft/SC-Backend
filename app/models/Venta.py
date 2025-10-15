from app.models import db
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy.dialects.postgresql import ENUM, NUMERIC, VARCHAR, TIMESTAMP
import uuid

vendido_por_enum = ENUM(
    'Lauren Vanegas',
    'Juan Obando',
    name='vendido_por_enum',
    create_type=True
)

metodo_pago_enum = ENUM(
    'Efectivo',
    'Nequi',
    name='metodo_pago_enum',
    create_type=True
)

tipo_venta_enum = ENUM(
    'Combo',
    'Individual',
    name='tipo_venta_enum',
    create_type=True
)

class Venta(db.Model):
    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)
    identificador_unico = db.Column(
        VARCHAR(36), unique=True, nullable=False,
        default=lambda: str(uuid.uuid4())
    )
    nombre_producto = db.Column(VARCHAR(100), nullable=False)
    precio = db.Column(NUMERIC(10, 2), nullable=False)
    fecha_venta = db.Column(
        TIMESTAMP(timezone=True),
        default=lambda: datetime.now(ZoneInfo("America/Bogota")),
        nullable=False
    )

    vendido_por = db.Column(vendido_por_enum, nullable=True)
    metodo_pago = db.Column(metodo_pago_enum, nullable=True)
    tipo_venta = db.Column(tipo_venta_enum, nullable=True)

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

    def __repr__(self):
        return f"<Venta id={self.id} producto={self.nombre_producto} tipo_venta={self.tipo_venta}>"
