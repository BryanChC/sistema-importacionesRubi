import usuariosLogin

def acceso_usuario(username, password):
    for usuario in usuariosLogin.usuarios:
        if usuario["username"] == username and usuario["password"] == password and usuario["estado"] == "activo":
            print("\nAcceso concedido.")
            print("Bienvenido: " + usuario["nombre"])
            print("Rol: " + usuario["rol"])
            return usuario

    print("\nUsuario o contraseña incorrectos.")
    return None

def mostrar_login():
    print("\n+=================================================+")
    print("|        BIENVENIDO - IMPORTACIONES RUBI S.A      |")
    print("+=================================================+")
    print("| Ingrese sus credenciales para acceder al sistema |")
    print("+-------------------------------------------------+")

def solicitar_credenciales():
    mostrar_login()
    username = input("Inserte usuario: ")
    password = input("Inserte password: ")
    usuario = acceso_usuario(username, password)
    return usuario

def obtener_rol(usuario):
    if usuario is None:
        return ""
    return usuario["rol"]