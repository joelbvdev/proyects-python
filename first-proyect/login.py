# Ejercicio:

# Crea un programa que simule un inicio de sesión:

# El sistema tiene guardado un usuario y una contraseña fija (por ejemplo: usuario = "joel", contraseña = "1234").

# El programa debe pedir al usuario que escriba su nombre de usuario y su contraseña.

# Si los datos coinciden con los guardados, debe mostrar: "Acceso concedido".

# Si no coinciden, mostrar: "Usuario o contraseña incorrectos".

# Después de 3 intentos fallidos, el programa debe bloquearse y mostrar: "Demasiados intentos, acceso denegado".

usuario_guardado = "Joel"
contraseña_guardado = "1234"

intentos_login = 0
intentos_contra = 0
intentos_usu = 0
acceso = False

while intentos_login < 3 and not acceso:
    intentos_login = intentos_login + 1
    ingrese_usuario = input("Ingrese su usuario:\n ")
    ingrese_contraseña = input("Ingrese su contraseña:\n ")

    if ingrese_usuario == usuario_guardado and ingrese_contraseña == contraseña_guardado:
            acceso = True
            print("Acceso Concedido!")
    elif ingrese_usuario == usuario_guardado and ingrese_contraseña != contraseña_guardado:
            print("La contraseña es incorrecta. Ingresela Nuevamente.")
            intentos_contra =+ 1
            ingrese_contraseña = input("Ingrese su contraseña:\n ")
            acceso = True
            print("Acceso Concedido")

    if ingrese_usuario != usuario_guardado and ingrese_contraseña != contraseña_guardado:
          print("Los datos no coinciden. Intente de Nuevo.")
    elif ingrese_usuario != usuario_guardado and ingrese_contraseña == contraseña_guardado:
          print("El usuario es incorrecto. Intento Nuevamente.")
          intentos_usu =+ 1
          ingrese_usuario = input("Ingrese su usuario:\n ")
          acceso = True
          print("Acceso Concedido")


if not acceso:
    print("Demasiados Intentos. Acceso denegado.")                                                                                       
        

    