class Persona:
#nombre,rut,apellido,edad,peso,altura
    def __init__(self):
        self.__nombre = input("Ingrese nombre: ")
        self.__apellido = input("Ingrese apellido: ")
        self.__rut = input("Ingrese rut: ")
        self.__edad = int(input("Ingrese edad: "))
        self.__peso = float(input("Ingrese peso: "))
        self.__altura = float(input("Ingrese altura: "))

    def get_nombre(self):
        return self.__nombre

    def mostrar(self):
        
        print(f'Nombre: {self.__nombre}')
        print(f'Apellido: {self.__apellido}')
        print(f'Rut: {self.__rut}')
        print(f'Edad: {self.__edad}')
        print(f'Peso: {self.__peso}')
        print(f'Altura: {self.__altura}')