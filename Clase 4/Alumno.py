from Persona import *
class Alumno(Persona):
    #nombre,rut,apellido,edad,peso,altura,notas,curso

    

    def __init__(self):
        super().__init__()
        self.__n_notas = int(input("Ingrese numero de notas: "))
        self.__curso = input("Ingrese curso: ") 
        self.__notas = []

    def mostrar(self):
        super().mostrar()
        print(f'N Notas: {self.__n_notas}')
        print(f'Curso: {self.__curso}')

    def registrar_notas(self):
        
        for nota in range(self.__n_notas):
            n = float(input(f'Ingrese nota {nota+1}: '))
            self.__notas.append(n)
        print(f"Notas: {self.__notas} ")

    def get_notas(self):
        return self.__notas

    