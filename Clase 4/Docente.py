from Persona import *
from Trabajador import Trabajador
class Docente(Persona,Trabajador):
    #nombre,rut,apellido,edad,peso,altura,especialidad
    def __init__(self):
        Persona.__init__(self)
        Trabajador.__init__(self)
        self.__especialidad = input("Ingrese especialidad: ")

    def mostrar(self):
        super().mostrar()
        print(f'Especialidad: {self.__especialidad}')

    