graph TD
    style MU_Backend fill:#f9f,stroke:#333,stroke-width:2px
    MU_Backend["MU-Backend"]

    %% App
    subgraph APP["app"] 
        style APP fill:#ffe0f0,stroke:#333,stroke-width:1px
        APP_models["models"]
        __init_app["__init__.py"]
        APP --> APP_models
        APP --> __init_app
        
        APP_models --> "CostoProducto.py"
        APP_models --> "Producto.py"
        APP_models --> "Usuario.py"
        APP_models --> "Venta.py"
        APP_models --> "__init__.py"
    end

    %% Routers
    subgraph ROUTERS["routers"]
        style ROUTERS fill:#ffdede,stroke:#333,stroke-width:1px
        ROUTERS_auth["auth"]
        ROUTERS_productos["productos"]
        ROUTERS_reportes["reportes"]
        ROUTERS_ventas["ventas"]
        __init_routers["__init__.py"]

        ROUTERS --> ROUTERS_auth
        ROUTERS --> ROUTERS_productos
        ROUTERS --> ROUTERS_reportes
        ROUTERS --> ROUTERS_ventas
        ROUTERS --> __init_routers

        ROUTERS_auth --> "login.py"
        ROUTERS_auth --> "registro.py"

        ROUTERS_productos --> "cambioEstado.py"
        ROUTERS_productos --> "consultar_producto.py"
        ROUTERS_productos --> "disolverCombo.py"
        ROUTERS_productos --> "eliminar_producto.py"
        ROUTERS_productos --> "registrar_producto.py"
        ROUTERS_productos --> "total_inventario.py"
        ROUTERS_productos --> "verCantidadProducto.py"
        ROUTERS_productos --> "verProductos.py"
        ROUTERS_productos --> "verProductosNombre.py"

        ROUTERS_reportes --> "exportar_combos.py"
        ROUTERS_reportes --> "exportar_inventario.py"
        ROUTERS_reportes --> "exportar_ventas.py"
        ROUTERS_reportes --> "margen_por_producto.py"
        ROUTERS_reportes --> "producto_detalle.py"
        ROUTERS_reportes --> "resumen_general.py"
        ROUTERS_reportes --> "top5_mas_vendidos.py"
        ROUTERS_reportes --> "ventasMes.py"

        ROUTERS_ventas --> "crearVenta.py"
        ROUTERS_ventas --> "crearVentaCombo.py"
        ROUTERS_ventas --> "margenVentas.py"
        ROUTERS_ventas --> "margen_combos.py"
        ROUTERS_ventas --> "ventaIdentificador.py"
        ROUTERS_ventas --> "ventasProductos.py"
        ROUTERS_ventas --> "verVentas.py"
    end

    %% Services
    subgraph SERVICES["services"]
        style SERVICES fill:#e0fff0,stroke:#333,stroke-width:1px
        SERVICES_auth["autenticacion"]
        SERVICES_productos["productos"]
        SERVICES_reportes["reportes"]
        SERVICES_ventas["ventas"]

        SERVICES --> SERVICES_auth
        SERVICES_auth --> "servicioInicioSesion.py"
        SERVICES_auth --> "servicioRegistro.py"

        SERVICES --> SERVICES_productos
        SERVICES_productos --> "servicioBuscarNombre.py"
        SERVICES_productos --> "servicioCambioEstado.py"
        SERVICES_productos --> "servicioCantidadProductos.py"
        SERVICES_productos --> "servicioConsultarProducto.py"
        SERVICES_productos --> "servicioDisolverCombo.py"
        SERVICES_productos --> "servicioEliminarProducto.py"
        SERVICES_productos --> "servicioRegistrarProducto.py"
        SERVICES_productos --> "servicioTotalInventario.py"
        SERVICES_productos --> "servicioVerProductos.py"

        SERVICES --> SERVICES_reportes
        SERVICES_reportes --> "servicioDetalleProducto.py"
        SERVICES_reportes --> "servicioExportarCombos.py"
        SERVICES_reportes --> "servicioExportarInventario.py"
        SERVICES_reportes --> "servicioExportarVentas.py"
        SERVICES_reportes --> "servicioMargenProducto.py"
        SERVICES_reportes --> "servicioResumenGeneral.py"
        SERVICES_reportes --> "servicioTop5.py"
        SERVICES_reportes --> "servicioVentasMes.py"

        SERVICES --> SERVICES_ventas
        SERVICES_ventas --> "servicioCrearCombo.py"
        SERVICES_ventas --> "servicioCrearVenta.py"
        SERVICES_ventas --> "servicioMargenCombos.py"
        SERVICES_ventas --> "servicioMargenVentas.py"
        SERVICES_ventas --> "servicioVentaIdentificador.py"
        SERVICES_ventas --> "servicioVentasNombre.py"
        SERVICES_ventas --> "servicioVerVentas.py"
    end

    %% Utils
    subgraph UTILS["utils"]
        style UTILS fill:#e0e0ff,stroke:#333,stroke-width:1px
        UTILS --> "auth_utils.py"
    end

    %% Conexiones con MU_Backend
    MU_Backend --> APP
    MU_Backend --> ROUTERS
    MU_Backend --> SERVICES
    MU_Backend --> UTILS
    MU_Backend --> ".env"
    MU_Backend --> ".gitignore"
    MU_Backend --> "app.py"
    MU_Backend --> "config.py"
    MU_Backend --> "requirements.txt"
    MU_Backend --> "backend_estructura.txt"
