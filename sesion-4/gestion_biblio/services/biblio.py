"""
Implementación del manejador de datos y archivos: el back-end del sistema.
"""

# importar anotaciones de tipo
# Union significa que una variable puede ser de varios tipos:
# -> variable: Union[int, float] --- significa que puede ser entero o flotante
import json
import os
from typing import Optional

from ..models import Libro


class Biblioteca:
    def __init__(self) -> None:
        # encontrar la direccion de raiz del sistema
        self.ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # ocupar la direccion raiz para crear la direccion del folder de datos
        self.ruta_registro = os.path.join(self.ruta_raiz, "data", "biblioteca.json")

        # asegurarse que los folders anteriores existen
        os.makedirs(os.path.dirname(self.ruta_registro), exist_ok=True)

        # leer los libros del archivo de registro
        self.libros: list[Libro] = []
        self.cargar_libros()

    def cargar_libros(self) -> bool:
        """
        Leer todos los libros en el archivo de registro
        para cargarlos y tenerlos en memoria.
        """

        try:
            with open(self.ruta_registro, "r") as registro:
                # leer el archivo json
                libros_data = json.load(registro)

                # retornar una lista de objetos Libro ocupando
                # los datos leidos del archivo de registro
                self.libros = [
                    Libro(
                        titulo=libro["titulo"],
                        autor=libro["autor"],
                        año=libro["año"],
                        isbn=libro["isbn"],
                    )
                    for libro in libros_data
                ]

                return True

        except (FileNotFoundError, json.JSONDecodeError):
            # si no existe el archivo, el registro esta vacio
            return False

    def guardar_libros(self) -> bool:
        """
        Guardar el registro en memoria actual al archivo de registro.
        """

        try:
            with open(self.ruta_registro, "w") as registro:
                # convertir todos los libros a diccionarios
                # para poder escribirlos en formato json
                libros_data: list[dict] = [libro.to_dict() for libro in self.libros]
                json.dump(libros_data, registro, indent=4)
            return True
        except Exception:
            # si hubo cualquier error, retornar False
            # para indicar que fallo la operacion
            return False

    def agregar_libro(self, libro: Libro) -> bool:
        """
        Agregar el libro recibido al registro.
        """

        self.cargar_libros()
        self.libros.append(libro)

        if self.guardar_libros():
            return True
        return False

    def mostrar_libros(self) -> Optional[str]:
        """
        Obtener todos los libros actualmente registrados.
        """

        if not self.cargar_libros():
            return None

        libros_formateados: str = ""

        for libro in self.libros:
            libros_formateados += libro.to_str()

        return libros_formateados

    def buscar_libro(self, buscando: str) -> Optional[str]:
        """
        Buscar un libro en el registro por titulo o ISBN.
        """

        self.cargar_libros()
        if not self.libros:
            return None

        # iterar sobre el registro para encontrar el
        # libro que coincida con el argumento dado
        libros_coincidentes: list[Libro] = [
            libro
            for libro in self.libros
            if buscando.lower() == libro.titulo.lower()
            or buscando.lower() == libro.isbn.lower()
        ]

        if not libros_coincidentes:
            # no se encontro el libro dado
            return None

        encontrado: str = ""

        for libro in self.libros:
            encontrado += libro.to_str()

        return encontrado

    def eliminar_libro(self, busqueda: str) -> bool:
        """
        Eliminar un libro del registro por título o ISBN.
        """

        self.cargar_libros()
        if not self.libros:
            return False

        cantidad_original = len(self.libros)

        # mantener solo los libros que no coincidan con el titulo/ISBN dado
        self.libros = [
            libro
            for libro in self.libros
            if busqueda.lower() != libro.titulo.lower()
            and busqueda.lower() != libro.isbn.lower()
        ]

        # si la longitud del registro es igual, no se encontro el libro dado
        if len(self.libros) == cantidad_original:
            return False

        # retornar el resultado de guardar al archivo
        return self.guardar_libros()
