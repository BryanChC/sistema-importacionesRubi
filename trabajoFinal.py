import accesosLogin
import usuariosLogin
import BD

sistema_activo = True

def pausar():
    input("\nPresione ENTER para continuar...")

def pedir_entero(mensaje):
    while True:
        dato = input(mensaje)
        try:
            numero = int(dato)
            return numero
        except ValueError:
            print("Debe ingresar un numero entero valido.")

def pedir_float(mensaje):
    while True:
        dato = input(mensaje)
        try:
            numero = float(dato)
            return numero
        except ValueError:
            print("Debe ingresar un numero valido. Ejemplo: 299.90")

def mostrar_titulo(titulo):
    print("\n+=================================================+")
    print("| " + titulo.center(47) + " |")
    print("+=================================================+")

def menu_administrador(usuario):
    global sistema_activo

    while sistema_activo == True:
        mostrar_titulo("MENU ADMINISTRADOR")
        print("| 1. Gestionar productos                          |")
        print("| 2. Gestionar usuarios                           |")
        print("| 3. Ver listado de ventas                        |")
        print("| 4. Cerrar sesion                                |")
        print("| 5. Salir del sistema                            |")
        print("+-------------------------------------------------+")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_usuarios()
        elif opcion == "3":
            BD.listar_ventas()
            pausar()
        elif opcion == "4":
            print("Sesion cerrada.")
            break
        elif opcion == "5":
            print("Saliendo del sistema...")
            sistema_activo = False
        else:
            print("Opcion incorrecta.")
            pausar()

def menu_productos():
    while True:
        mostrar_titulo("CRUD DE PRODUCTOS")
        print("| 1. Listar productos                             |")
        print("| 2. Buscar producto por codigo                   |")
        print("| 3. Buscar producto por nombre                   |")
        print("| 4. Agregar producto                             |")
        print("| 5. Actualizar producto                          |")
        print("| 6. Eliminar producto                            |")
        print("| 7. Volver                                      |")
        print("+-------------------------------------------------+")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            BD.listar_productos()
            pausar()
        elif opcion == "2":
            codigo = input("Ingrese codigo del producto: ")
            producto = BD.buscar_producto_por_codigo(codigo)
            BD.mostrar_producto(producto)
            pausar()
        elif opcion == "3":
            nombre = input("Ingrese nombre o parte del nombre: ")
            encontrados = BD.buscar_producto_por_nombre(nombre)
            if len(encontrados) == 0:
                print("No se encontraron productos.")
            else:
                for producto in encontrados:
                    BD.mostrar_producto(producto)
            pausar()
        elif opcion == "4":
            agregar_producto()
            pausar()
        elif opcion == "5":
            codigo = input("Ingrese codigo del producto a actualizar: ")
            BD.actualizar_producto(codigo)
            pausar()
        elif opcion == "6":
            codigo = input("Ingrese codigo del producto a eliminar: ")
            BD.eliminar_producto(codigo)
            pausar()
        elif opcion == "7":
            break
        else:
            print("Opcion incorrecta.")
            pausar()

def agregar_producto():
    print("\n----- AGREGAR PRODUCTO -----")
    codigo = input("Codigo de producto: ")
    nombre = input("Nombre de producto: ")
    categoria = input("Categoria: ")
    stock = pedir_entero("Stock: ")
    precio_venta = pedir_float("Precio de venta: ")

    if stock < 0:
        print("El stock no puede ser negativo.")
        return

    if precio_venta <= 0:
        print("El precio debe ser mayor que cero.")
        return

    BD.crear_producto(codigo, nombre, categoria, stock, precio_venta)

def menu_usuarios():
    while True:
        mostrar_titulo("GESTION DE USUARIOS")
        print("| 1. Listar usuarios                              |")
        print("| 2. Buscar usuario                               |")
        print("| 3. Agregar usuario                              |")
        print("| 4. Actualizar usuario                           |")
        print("| 5. Eliminar usuario                             |")
        print("| 6. Mostrar total de usuarios                    |")
        print("| 7. Volver                                      |")
        print("+-------------------------------------------------+")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            usuariosLogin.listar_usuarios()
            pausar()
        elif opcion == "2":
            dato = input("Ingrese nombre, DNI o usuario: ")
            usuariosLogin.buscar_empleado(dato)
            pausar()
        elif opcion == "3":
            agregar_usuario()
            pausar()
        elif opcion == "4":
            username = input("Ingrese el usuario a actualizar: ")
            usuariosLogin.actualizar_usuario(username)
            pausar()
        elif opcion == "5":
            username = input("Ingrese el usuario a eliminar: ")
            usuariosLogin.eliminar_usuario(username)
            pausar()
        elif opcion == "6":
            usuariosLogin.total_empleados()
            pausar()
        elif opcion == "7":
            break
        else:
            print("Opcion incorrecta.")
            pausar()

def agregar_usuario():
    print("\n----- AGREGAR USUARIO -----")
    nombre = input("Nombre completo: ")
    dni = input("DNI: ")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    rol = input("Rol administrador/vendedor: ")

    usuariosLogin.crear_usuario(nombre, dni, username, password, rol)

def menu_vendedor(usuario):
    global sistema_activo

    while sistema_activo == True:
        mostrar_titulo("MENU VENDEDOR")
        print("| 1. Ver productos disponibles                    |")
        print("| 2. Buscar producto                              |")
        print("| 3. Realizar venta                               |")
        print("| 4. Cerrar sesion                                |")
        print("| 5. Salir del sistema                            |")
        print("+-------------------------------------------------+")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            BD.listar_productos_con_stock()
            pausar()
        elif opcion == "2":
            codigo = input("Ingrese codigo del producto: ")
            producto = BD.buscar_producto_por_codigo(codigo)
            BD.mostrar_producto(producto)
            pausar()
        elif opcion == "3":
            realizar_venta(usuario)
            pausar()
        elif opcion == "4":
            print("Sesion cerrada.")
            break
        elif opcion == "5":
            print("Saliendo del sistema...")
            sistema_activo = False
        else:
            print("Opcion incorrecta.")
            pausar()

def realizar_venta(usuario):
    print("\n----- REALIZAR VENTA -----")
    BD.listar_productos_con_stock()
    codigo = input("Ingrese codigo del producto a vender: ")
    cantidad = pedir_entero("Ingrese cantidad a vender: ")

    BD.registrar_venta(codigo, cantidad, usuario["nombre"])

def iniciar_sistema():
    global sistema_activo

    while sistema_activo == True:
        usuario = accesosLogin.solicitar_credenciales()

        if usuario is None:
            reintentar = input("¿Desea intentar nuevamente? S/N: ")
            if reintentar.upper() != "S":
                print("Saliendo del sistema...")
                sistema_activo = False
        else:
            rol = accesosLogin.obtener_rol(usuario)

            if rol == "administrador":
                menu_administrador(usuario)
            elif rol == "vendedor":
                menu_vendedor(usuario)
            else:
                print("Rol no reconocido.")

if __name__ == "__main__":
    iniciar_sistema()