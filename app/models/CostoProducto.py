from app.models import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import VARCHAR, NUMERIC, TIMESTAMP

class CostoProducto(db.Model):
    __tablename__ = 'costos_producto'  

    id = db.Column(db.Integer, primary_key=True)
    identificador_producto = db.Column(VARCHAR(36), nullable=False)
    precio_compra = db.Column(NUMERIC(10, 2), nullable=False)
    fecha_registro = db.Column(
        TIMESTAMP(timezone=True),
        server_default=db.func.now(),  
        nullable=False
    )

    def __repr__(self):
        return f"<CostoProducto id={self.id} identificador_producto={self.identificador_producto}>"
