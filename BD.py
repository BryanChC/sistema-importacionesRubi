from datetime import datetime

productos = [
    {
        "codigo": "P001",
        "nombre": "Licuadora Oster",
        "categoria": "Pequeño electrodomestico",
        "stock": 8,
        "precio_venta": 299.00,
        "estado": "activo"
    },
    {
        "codigo": "P002",
        "nombre": "Televisor Samsung 32",
        "categoria": "Linea marron",
        "stock": 5,
        "precio_venta": 899.00,
        "estado": "activo"
    },
    {
        "codigo": "P003",
        "nombre": "Refrigeradora LG",
        "categoria": "Linea blanca",
        "stock": 3,
        "precio_venta": 1899.00,
        "estado": "activo"
    }
]

ventas = []

def generar_numero_venta():
    numero = len(ventas) + 1
    return "V" + str(numero).zfill(5)

def buscar_producto_por_codigo(codigo):
    for producto in productos:
        if producto["codigo"].upper() == codigo.upper() and producto["estado"] == "activo":
            return producto
    return None

def buscar_producto_por_nombre(nombre):
    encontrados = []
    for producto in productos:
        if producto["estado"] == "activo":
            if nombre.lower() in producto["nombre"].lower():
                encontrados.append(producto)
    return encontrados

def listar_productos():
    print("\n+-------------------------------------------------------------------------------+")
    print("|                              LISTADO DE PRODUCTOS                              |")
    print("+----------+------------------------------+----------------------+-------+--------+")
    print("| Codigo   | Nombre                       | Categoria            | Stock | Precio |")
    print("+----------+------------------------------+----------------------+-------+--------+")

    hay_productos = False
    for producto in productos:
        if producto["estado"] == "activo":
            hay_productos = True
            codigo = producto["codigo"][:8].ljust(8)
            nombre = producto["nombre"][:28].ljust(28)
            categoria = producto["categoria"][:20].ljust(20)
            stock = str(producto["stock"]).rjust(5)
            precio = ("S/" + format(producto["precio_venta"], ".2f")).rjust(6)
            print("| " + codigo + " | " + nombre + " | " + categoria + " | " + stock + " | " + precio + " |")

    if hay_productos == False:
        print("| No hay productos registrados.                                                   |")

    print("+----------+------------------------------+----------------------+-------+--------+")

def listar_productos_con_stock():
    print("\n+-------------------------------------------------------------------------------+")
    print("|                         PRODUCTOS DISPONIBLES PARA VENTA                       |")
    print("+----------+------------------------------+----------------------+-------+--------+")
    print("| Codigo   | Nombre                       | Categoria            | Stock | Precio |")
    print("+----------+------------------------------+----------------------+-------+--------+")

    hay_productos = False
    for producto in productos:
        if producto["estado"] == "activo" and producto["stock"] > 0:
            hay_productos = True
            codigo = producto["codigo"][:8].ljust(8)
            nombre = producto["nombre"][:28].ljust(28)
            categoria = producto["categoria"][:20].ljust(20)
            stock = str(producto["stock"]).rjust(5)
            precio = ("S/" + format(producto["precio_venta"], ".2f")).rjust(6)
            print("| " + codigo + " | " + nombre + " | " + categoria + " | " + stock + " | " + precio + " |")

    if hay_productos == False:
        print("| No hay productos con stock disponible.                                          |")

    print("+----------+------------------------------+----------------------+-------+--------+")

def mostrar_producto(producto):
    if producto is None:
        print("Producto no encontrado.")
        return

    print("\n----------------------------------------")
    print("Codigo: " + producto["codigo"])
    print("Nombre: " + producto["nombre"])
    print("Categoria: " + producto["categoria"])
    print("Stock: " + str(producto["stock"]))
    print("Precio de venta: S/" + format(producto["precio_venta"], ".2f"))
    print("----------------------------------------")

def crear_producto(codigo, nombre, categoria, stock, precio_venta):
    if buscar_producto_por_codigo(codigo) is not None:
        print("No se puede crear el producto. El codigo ya existe.")
        return False

    nuevo_producto = {
        "codigo": codigo.upper(),
        "nombre": nombre,
        "categoria": categoria,
        "stock": stock,
        "precio_venta": precio_venta,
        "estado": "activo"
    }

    productos.append(nuevo_producto)
    print("Producto creado correctamente.")
    return True

def actualizar_producto(codigo):
    producto = buscar_producto_por_codigo(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return False

    print("\nDejar en blanco si no desea modificar el dato.")
    nuevo_nombre = input("Nuevo nombre: ")
    nueva_categoria = input("Nueva categoria: ")
    nuevo_stock = input("Nuevo stock: ")
    nuevo_precio = input("Nuevo precio de venta: ")

    if nuevo_nombre != "":
        producto["nombre"] = nuevo_nombre

    if nueva_categoria != "":
        producto["categoria"] = nueva_categoria

    if nuevo_stock != "":
        try:
            stock_convertido = int(nuevo_stock)
            if stock_convertido < 0:
                print("El stock no puede ser negativo.")
                return False
            producto["stock"] = stock_convertido
        except ValueError:
            print("Stock invalido.")
            return False

    if nuevo_precio != "":
        try:
            precio_convertido = float(nuevo_precio)
            if precio_convertido <= 0:
                print("El precio debe ser mayor que cero.")
                return False
            producto["precio_venta"] = precio_convertido
        except ValueError:
            print("Precio invalido.")
            return False

    print("Producto actualizado correctamente.")
    return True

def eliminar_producto(codigo):
    producto = buscar_producto_por_codigo(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return False

    confirmacion = input("¿Seguro que desea eliminar/desactivar este producto? S/N: ")
    if confirmacion.upper() == "S":
        producto["estado"] = "inactivo"
        print("Producto eliminado correctamente.")
        return True
    else:
        print("Operacion cancelada.")
        return False

def registrar_venta(codigo_producto, cantidad, vendedor):
    producto = buscar_producto_por_codigo(codigo_producto)

    if producto is None:
        print("Producto no encontrado.")
        return False

    if producto["stock"] <= 0:
        print("No se puede vender. El producto no cuenta con stock.")
        return False

    if cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
        return False

    if cantidad > producto["stock"]:
        print("No se puede vender. Stock insuficiente.")
        print("Stock disponible: " + str(producto["stock"]))
        return False

    subtotal = producto["precio_venta"] * cantidad
    igv = subtotal * 0.18
    total = subtotal + igv

    venta = {
        "numero": generar_numero_venta(),
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "vendedor": vendedor,
        "codigo_producto": producto["codigo"],
        "nombre_producto": producto["nombre"],
        "categoria": producto["categoria"],
        "cantidad": cantidad,
        "precio_unitario": producto["precio_venta"],
        "subtotal": subtotal,
        "igv": igv,
        "total": total
    }

    ventas.append(venta)

    producto["stock"] = producto["stock"] - cantidad

    print("\nVenta registrada correctamente.")
    imprimir_boleta(venta)
    return True

def imprimir_boleta(venta):
    print("\n+====================================================+")
    print("|              IMPORTACIONES RUBI S.A                |")
    print("|                    BOLETA DE VENTA                 |")
    print("+====================================================+")
    print("Nro: " + venta["numero"] + "        Fecha: " + venta["fecha"])
    print("Vendedor: " + venta["vendedor"])
    print("------------------------------------------------------")
    print("Producto: " + venta["nombre_producto"])
    print("Codigo: " + venta["codigo_producto"])
    print("Cantidad: " + str(venta["cantidad"]))
    print("Precio unitario: S/" + format(venta["precio_unitario"], ".2f"))
    print("------------------------------------------------------")
    print("Subtotal: S/" + format(venta["subtotal"], ".2f"))
    print("IGV 18%:  S/" + format(venta["igv"], ".2f"))
    print("TOTAL:    S/" + format(venta["total"], ".2f"))
    print("+====================================================+")

def listar_ventas():
    print("\n+----------------------------------------------------------------------------------------------------+")
    print("|                                      LISTADO DE VENTAS                                             |")
    print("+----------+---------------------+---------------+----------+--------------------------+------+-------+")
    print("| Nro      | Fecha               | Vendedor      | Codigo   | Producto                 | Cant | Total |")
    print("+----------+---------------------+---------------+----------+--------------------------+------+-------+")

    if len(ventas) == 0:
        print("| No hay ventas registradas.                                                                        |")
    else:
        for venta in ventas:
            numero = venta["numero"][:8].ljust(8)
            fecha = venta["fecha"][:19].ljust(19)
            vendedor = venta["vendedor"][:13].ljust(13)
            codigo = venta["codigo_producto"][:8].ljust(8)
            producto = venta["nombre_producto"][:24].ljust(24)
            cantidad = str(venta["cantidad"]).rjust(4)
            total = ("S/" + format(venta["total"], ".2f")).rjust(5)
            print("| " + numero + " | " + fecha + " | " + vendedor + " | " + codigo + " | " + producto + " | " + cantidad + " | " + total + " |")

    print("+----------+---------------------+---------------+----------+--------------------------+------+-------+")