from app.models import db
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy.dialects.postgresql import ENUM, NUMERIC, VARCHAR, TIMESTAMP

producto_estado_enum = ENUM(
    'inventario',
    'vendido',
    name='estado_producto',
    create_type=True  
)

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    identificador_unico = db.Column(VARCHAR(36), unique=True, nullable=False)
    nombre = db.Column(VARCHAR(100), nullable=False)
    precio = db.Column(NUMERIC(10, 2), nullable=False)
    estado = db.Column(producto_estado_enum, nullable=False, server_default='inventario')
    fecha_creacion = db.Column(
        TIMESTAMP(timezone=True),
        default=lambda: datetime.now(ZoneInfo("America/Bogota")),
        nullable=False
    )

    def __repr__(self):
        return f"<Producto id={self.id} nombre={self.nombre} estado={self.estado}>"
