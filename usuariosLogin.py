roles_validos = ["administrador", "vendedor"]

usuarios = [
    {
        "id": 1,
        "nombre": "Administrador Principal",
        "dni": "00000000",
        "username": "Ryax",
        "password": "Sheldon25*",
        "rol": "administrador",
        "estado": "activo"
    },
    {
        "id": 2,
        "nombre": "Vendedor Demo",
        "dni": "11111111",
        "username": "vendedor1",
        "password": "1234",
        "rol": "vendedor",
        "estado": "activo"
    }
]

def generar_id_usuario():
    if len(usuarios) == 0:
        return 1
    ultimo_id = 0
    for usuario in usuarios:
        if usuario["id"] > ultimo_id:
            ultimo_id = usuario["id"]
    return ultimo_id + 1

def validar_rol(rol):
    rol = rol.lower().strip()
    for r in roles_validos:
        if r == rol:
            return True
    return False

def buscar_usuario_por_username(username):
    for usuario in usuarios:
        if usuario["username"] == username and usuario["estado"] == "activo":
            return usuario
    return None

def buscar_usuario_por_dni(dni):
    for usuario in usuarios:
        if usuario["dni"] == dni and usuario["estado"] == "activo":
            return usuario
    return None

def existe_empleado(nombre, dni_ingresado):
    for i in range(len(usuarios)):
        if usuarios[i]["nombre"].lower() == nombre.lower() and usuarios[i]["dni"] == dni_ingresado and usuarios[i]["estado"] == "activo":
            return True
    return False

def buscar_empleado(dato):
    encontrado = False

    for i in range(len(usuarios)):
        if usuarios[i]["estado"] == "activo":
            if usuarios[i]["nombre"].lower() == dato.lower() or usuarios[i]["dni"] == dato or usuarios[i]["username"] == dato:
                encontrado = True
                print("----------------------------------------")
                print("Usuario encontrado")
                print("ID: " + str(usuarios[i]["id"]))
                print("Nombre: " + usuarios[i]["nombre"])
                print("DNI: " + usuarios[i]["dni"])
                print("Usuario: " + usuarios[i]["username"])
                print("Rol: " + usuarios[i]["rol"])
                print("----------------------------------------")

    if encontrado == False:
        print("Usuario no encontrado")

def total_empleados():
    total = 0
    for usuario in usuarios:
        if usuario["estado"] == "activo":
            total = total + 1
    print("Total de usuarios registrados: " + str(total))

def listar_usuarios():
    print("\n+------------------------------------------------------------+")
    print("|                  LISTADO DE USUARIOS                       |")
    print("+----+--------------------------+------------+---------------+")
    print("| ID | Nombre                   | Usuario    | Rol           |")
    print("+----+--------------------------+------------+---------------+")

    hay_usuarios = False
    for usuario in usuarios:
        if usuario["estado"] == "activo":
            hay_usuarios = True
            id_txt = str(usuario["id"]).ljust(2)
            nombre_txt = usuario["nombre"][:24].ljust(24)
            username_txt = usuario["username"][:10].ljust(10)
            rol_txt = usuario["rol"][:13].ljust(13)
            print("| " + id_txt + " | " + nombre_txt + " | " + username_txt + " | " + rol_txt + " |")

    if hay_usuarios == False:
        print("| No hay usuarios registrados.                               |")

    print("+----+--------------------------+------------+---------------+")

def crear_usuario(nombre, dni, username, password, rol):
    if validar_rol(rol) == False:
        print("Rol incorrecto. Solo se permite administrador o vendedor.")
        return False

    if buscar_usuario_por_username(username) is not None:
        print("No se puede crear el usuario. El nombre de usuario ya existe.")
        return False

    if buscar_usuario_por_dni(dni) is not None:
        print("No se puede crear el usuario. El DNI ya existe.")
        return False

    nuevo_usuario = {
        "id": generar_id_usuario(),
        "nombre": nombre,
        "dni": dni,
        "username": username,
        "password": password,
        "rol": rol.lower().strip(),
        "estado": "activo"
    }

    usuarios.append(nuevo_usuario)
    print("Usuario creado correctamente.")
    return True

def actualizar_usuario(username):
    usuario = buscar_usuario_por_username(username)

    if usuario is None:
        print("Usuario no encontrado.")
        return False

    print("\nDejar en blanco si no desea modificar el dato.")
    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_dni = input("Nuevo DNI: ")
    nuevo_password = input("Nueva contraseña: ")
    nuevo_rol = input("Nuevo rol administrador/vendedor: ")

    if nuevo_nombre != "":
        usuario["nombre"] = nuevo_nombre

    if nuevo_dni != "":
        existe_dni = buscar_usuario_por_dni(nuevo_dni)
        if existe_dni is not None and existe_dni["username"] != usuario["username"]:
            print("No se puede actualizar. Ese DNI ya pertenece a otro usuario.")
            return False
        usuario["dni"] = nuevo_dni

    if nuevo_password != "":
        usuario["password"] = nuevo_password

    if nuevo_rol != "":
        if validar_rol(nuevo_rol) == False:
            print("Rol incorrecto. Solo se permite administrador o vendedor.")
            return False
        usuario["rol"] = nuevo_rol.lower().strip()

    print("Usuario actualizado correctamente.")
    return True

def eliminar_usuario(username):
    usuario = buscar_usuario_por_username(username)

    if usuario is None:
        print("Usuario no encontrado.")
        return False

    if usuario["username"] == "Ryax":
        print("No se puede eliminar el administrador principal del sistema.")
        return False

    confirmacion = input("¿Seguro que desea eliminar/desactivar este usuario? S/N: ")
    if confirmacion.upper() == "S":
        usuario["estado"] = "inactivo"
        print("Usuario eliminado correctamente.")
        return True
    else:
        print("Operacion cancelada.")
        return False