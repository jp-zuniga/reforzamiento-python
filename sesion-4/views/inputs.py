"""
Implementación de la clase Inputs, la cual
se encarga de pedirle datos a los usuarios.
"""


from services.biblioService import Biblioteca
from models.autor import Autor
from models.libro import Libro
import random


class Inputs:
    def __init__(self):
        pass

    def case_one(self):
        biblioteca: Biblioteca = Biblioteca()
        titulo = input("Ingrese el titulo: ")
        while True:
            counter = input("Ingrese la cantidad de autores: ")
            if counter.isdigit():
                break
        autores = []
        for i in range(int(counter)):
            nombre = input(f"Ingrese el Nombre del Autor {i + 1}: ")
            apellido = input(f"Ingrese el Apellido del Autor {i + 1}: ")
            autores.append(Autor(nombre, apellido))
        while True:
            año = input("Ingrese el año del libro: ")
            if not año.isdigit():
                print("Año incorrecto, ingrese nuevamente...")
            else:
                break
        edicion = input("Ingrese la edicion del libro: ")
        libro = Libro(titulo, autores, int(año), edicion, random.randint(1000, 9999))
        biblioteca.agregar_libro(libro.to_dict())

        return

    def case_two(self):
        biblioteca: Biblioteca = Biblioteca()
        biblioteca.mostrar_libros()
        return

    def case_three(self):
        biblioteca: Biblioteca = Biblioteca()
        opc_search = input("Ingrese el titulo o isbn a buscar: ")
        biblioteca.buscar_libro(opc_search)
        return

    def case_four(self):
        biblioteca: Biblioteca = Biblioteca()
        isbn = int(input("Ingrese el isbn del libro a eliminar: "))
        biblioteca.eliminar_libro(isbn)
