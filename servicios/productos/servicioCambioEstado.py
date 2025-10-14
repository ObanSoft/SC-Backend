from app.models import db
from app.models.Producto import Producto
from app.models.Venta import Venta  

def cambiar_estado_producto(identificador_unico: str):
    producto = Producto.query.filter_by(identificador_unico=identificador_unico).first()

    if not producto:
        return {"error": "Producto no encontrado"}, 404

    if producto.estado == "vendido":
        producto.estado = "inventario"

        venta = Venta.query.filter_by(identificador_unico=identificador_unico).first()
        if venta:
            db.session.delete(venta)

    else:
        return {"error": "No se puede cambiar un producto de inventario a vendido"}, 400

    try:
        db.session.commit()
        return {
            "mensaje": f"Estado del producto '{producto.nombre}' actualizado a '{producto.estado}'"
        }, 200
    except Exception as e:
        db.session.rollback()
        return {"error": "No se pudo actualizar el estado", "detalle": str(e)}, 500
