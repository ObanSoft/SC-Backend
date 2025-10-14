from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .Producto import Producto
from .Venta import Venta
from .CostoProducto import CostoProducto
