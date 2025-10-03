# REGISTRO DE ALUMNOS


ingrese_nombre = input("Ingrese nombre del alumno: ")
ingrese_edad = int(input("Ingrese la edad: "))
ingrese_nota = int(input("Ingrese nota: "))

def validar_nombre():
    validar = ingrese_nombre.isalpha() 
    return validar

def validar_edad():
    validar = ingrese_edad >= 18
    return validar

def validar_nota():
    validar = ingrese_nota > 0 and ingrese_nota < 10
    return validar

if ingrese_nota >= 6:
    estado = "Aprobado"
elif ingrese_nota < 6:
    estado = "Desaprobado"

print("Alumno:", ingrese_nombre, "| Edad:", ingrese_edad, "| Nota:", ingrese_nota, "| Estado:", estado)
