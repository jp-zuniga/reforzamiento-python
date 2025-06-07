"""
Implementación de la clase Libro.
"""

# importar anotaciones de tipo
# Union significa que una variable puede ser de varios tipos:
# -> variable: Union[int, float] --- significa que puede ser entero o flotante
from typing import Union


class Libro:
    def __init__(self, titulo: str, autor: str, año: int, isbn: str) -> None:
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.isbn = isbn

    def to_dict(self) -> dict[str, Union[int, str]]:
        """
        Convierte un objeto Libro a un diccionario, para poder
        guardarlos como un objeto JSON en el archivo de registro.
        """

        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "año": self.año,
            "isbn": self.isbn,
        }

    def to_str(self) -> str:
        """
        Convierte la instancia a un string para poder representar
        un Libro de una manera legible para el usuario.
        """

        instancia = self.to_dict()
        str_libro = ""

        str_libro += f"Título: {instancia['titulo']}\n"
        str_libro += f"Autor: {instancia['autor']}\n"
        str_libro += f"ISBN: {instancia['isbn']}\n"
        str_libro += f"Año: {instancia['año']}\n"
        str_libro += f"\n{'=' * 50}\n\n"

        return str_libro
