from datetime import datetime
from app.models import db
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    numero_identificacion = db.Column(VARCHAR(50), unique=True, nullable=False)
    contrasena = db.Column(VARCHAR(255), nullable=False)
    fecha_creacion = db.Column(
        TIMESTAMP(timezone=True), 
        server_default=db.func.now(), 
        nullable=False
    )

    def __repr__(self):
        return f"<Usuario id={self.id} numero_identificacion={self.numero_identificacion}>"
