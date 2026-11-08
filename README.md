# TiendaPy

Creación de programa en Python para controlar un inventario y ventas de una tienda de barrio planteada por el proyecto (caso de estudio: tienda "Don Aurelio"). Proyecto final del curso Python 0 a 100 – ACM.

**Autores:** Tatiana Andrea Moreno Suarez (20262020136) y Sara Sofia Angulo Salcedo (20262020138)

## Funcionalidades

- **Inventario:** registrar, consultar, modificar y eliminar productos; búsqueda por código o categoría.
- **Ventas:** carrito con varios productos, descuento automático (5 % desde $50 000 y 10 % desde $100 000), pago, cambio y descuento de stock.
- **Alertas:** productos con stock menor o igual al mínimo, agrupados por proveedor, con los agotados identificados.
- **Cierre del día:** total vendido, número de transacciones, ticket promedio, producto más vendido, productos sin ventas y categorías con movimiento.
- **Persistencia:** el inventario y el historial de ventas se guardan en archivos de texto plano y se conservan entre ejecuciones.

## Estructura

```
TiendaPy/
|-- README.md
|-- DATA/
|   |-- inventario.txt
|   `-- ventas.txt
`-- SRC/
    |-- main.py            # menú principal
    |-- inventario.py      # CRUD de productos
    |-- ventas.py          # carrito, descuentos y cambio
    |-- reportes.py        # alertas y cierre del día
    |-- persistencia.py    # lectura y escritura de archivos
    `-- validaciones.py    # captura segura de datos
```

## Cómo ejecutarlo

Requiere Python 3.8 o superior. No usa librerías externas.

```bash
# opcional: crear y activar un entorno virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

python SRC/main.py
```

## Formato de los archivos

`DATA/inventario.txt`: un producto por línea, campos separados por `|`:

```
codigo|nombre|categoria|precio|stock|stock_minimo|proveedor
LAC001|Leche entera 1L|Lacteos|4200.0|35|10|Alqueria
```

`DATA/ventas.txt`: una venta por línea, con formato `fecha|total|codigo:cantidad;codigo:cantidad`:

```
2026-11-20|18400.0|LAC001:2;BEB003:1
```

Si una línea de cualquiera de los dos archivos está dañada, se omite con una advertencia y el programa continúa con las demás.

## Decisiones de diseño

- Se usaron diccionarios y listas nativas (sin clases) para modelar productos, carrito y ventas.
- Toda la lectura y escritura de archivos está en `persistencia.py`; los demás módulos no abren archivos directamente.
- El inventario se guarda en un archivo temporal que luego reemplaza al original, para que un error durante la escritura no deje el inventario dañado.
