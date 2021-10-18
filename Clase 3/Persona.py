#Constructor
#atributos
#getters y setters
#metodos
#encapsulamiento
class Persona:


    def __init__(self,rut,nombre,apellido):
        self.__rut = rut
        self.__nombre = nombre #Si parte con dos guion bajo, es privado
        self.__apellido = apellido

    def mostrar(self):
        print(f'Rut: {self.__rut}')
        print(f'Nombre: {self.__nombre}')
        print(f'Apellido: {self.__apellido}')

    def get_rut(self):
        return self.__rut

