from Persona import *

def mostrar():
    for alumno in alumnos:
        alumno.mostrar()


alumnos = []
for x in range(3):
    rut = input("Ingrese su rut: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    a = Persona(rut,nombre,apellido)
    alumnos.append(a)

mostrar()

print()
rut = input("Ingrese rut a buscar")
for alumno in alumnos:
    if alumno.get_rut() == rut:
        alumno.mostrar()

print()
rut = input("Ingrese rut a eliminar")
for alumno in alumnos:
    if alumno.get_rut() == rut:
        alumnos.remove(alumno)

mostrar()

