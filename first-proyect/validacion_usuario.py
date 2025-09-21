# 🚀 Proyecto propuesto (versión simple): Validador de Contacto

# 👉 La idea: el usuario ingresa un nombre y un teléfono, y el programa valida:

# Que el nombre sea solo letras.

# Que el teléfono sea solo números.

# Devuelve un mensaje con el resultado.

def validar_usuario(usuario, telefono):
    mensaje = ""
    if not usuario.isalpha():
        mensaje = "El Usuario no es valido!. Ingrese Nuevamente."
    elif not telefono.isdigit():
        mensaje = "El telefono no es valido!. Ingrese Nuevamente"
    else:
        mensaje = f"CONTACTO VALIDO: {usuario}, {telefono}"
    return mensaje

print("VALIDACION DE CONTACTO")
ingrese_usuario = input("Ingrese su Usuario: ")
ingrese_telefono = input("Ingrese su Telefono: ")
validar_usuario(ingrese_usuario, ingrese_telefono)

# TEST DEL PROGRAMA
def test_validar_usuario():
    assert(validar_usuario ("Joel", "6464564") == "CONTACTO VALIDO: Joel, 6464564")
    assert(validar_usuario ("Joel", "---") == "El telefono no es valido!. Ingrese Nuevamente")
    assert(validar_usuario ("123", "hghg") == "El Usuario no es valido!. Ingrese Nuevamente.")
    print("LOS TEST PASARON CORRECTAMENTE")

test_validar_usuario()