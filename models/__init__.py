from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importa los modelos aquí para que se registren en db.metadata
from .Producto import Producto
from .Venta import Venta
from .CostoProducto import CostoProducto
