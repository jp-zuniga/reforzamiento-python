from services.biblioService import Biblioteca
from models.autores import Autores
from models.book import Book
import random

class Inputs:
    def __init__(self):
        pass
    
    def case_one(self):
        biblioteca: Biblioteca = Biblioteca()
        titulo = input("Ingrese el titulo: ")
        while True:
            counter = input("Ingrese la cantidad de autores: ")
            if counter.isdigit(): break
        autores = []
        for i in range(int(counter)):
            nombre = input(f"Ingrese el Nombre del Autor {i+1}: ")
            apellido = input(f"Ingrese el Apellido del Autor {i+1}: ")
            autores.append(Autores(nombre, apellido))
        while True:
            anio = input("Ingrese el año del libro: ")
            if not anio.isdigit():
                print("Año incorrecto, ingrese nuevamente...")
            else:
                break
        edicion = input("Ingrese la edicion del libro: ")
        libro = Book(titulo, autores, int(anio), edicion, random.randint(1000, 9999))
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