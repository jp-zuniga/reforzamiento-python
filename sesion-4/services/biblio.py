"""
Implementación de la clase Biblioteca, la cual se
encarga de manejar el backend de nuestro sistema.
"""


import json
import os


class Biblioteca:
    def __init__(self):
        self.libro = dict()
        self.ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.ruta_registro = os.path.join(self.ruta_raiz, "data", "biblioteca.json")

    def agregar_libro(self, libro):
        self.libro = libro
        registro_actual = []
        os.makedirs(os.path.dirname(self.ruta_registro), exist_ok=True)

        try:
            with open(self.ruta_registro, "r") as registro:
                registro_actual = json.load(registro)
        except FileNotFoundError:
            registro_actual = []

        registro_actual.append(self.libro)

        with open(self.ruta_registro, "w") as registro:
            json.dump(registro_actual, registro, indent=4)
        print("Libro registrado...")

    def mostrar_libros(self):
        try:
            with open(self.ruta_registro, "r") as registro:
                registros = json.load(registro)

                if not registros:
                    print("Sin registros...")
                    return

                for i, libro in enumerate(registros, start=1):
                    print(
                        f"Registro {i}:\n\tTitulo: {libro['titulo']}\n\tAutores: {libro['autores']}\n\taño: {libro['año']}\n\tEdicion: {libro['edicion']}\n\tISBN: {libro['isbn']}"
                    )
        except FileNotFoundError:
            print("Archivo no encontrado...")
            return

    def buscar_libro(self, opc_search):
        try:
            with open(self.ruta_registro, "r") as registro:
                registros = json.load(registro)

            try:
                opc_search_int = int(opc_search)
            except ValueError:
                opc_search_int = None

            match = [
                libro
                for libro in registros
                if libro["titulo"].lower() == opc_search.lower()
                or (opc_search_int is not None and libro["isbn"] == opc_search_int)
            ]

            if match:
                for i, libro in enumerate(match, start=1):
                    print(
                        f"Registro {i}:\n\tTitulo: {libro['titulo']}\n\tAutores: {libro['autores']}\n\taño: {libro['año']}\n\tEdicion: {libro['edicion']}\n\tISBN: {libro['isbn']}"
                    )

            else:
                print("No se encontro el registro...")

        except FileNotFoundError:
            print("Archivo no encontrado...")
            return

    def eliminar_libro(self, isbn_search):
        try:
            with open(self.ruta_registro, "r") as registro:
                registros = json.load(registro)

            nuevo_registro = [
                libro for libro in registros if libro["isbn"] != isbn_search
            ]

            with open(self.ruta_registro, "w") as registro:
                json.dump(nuevo_registro, registro, indent=4)
            print("Libro registrado...")

        except FileNotFoundError:
            print("Archivo no encontrado...")
            return
