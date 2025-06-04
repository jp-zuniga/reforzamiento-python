"""
Implementación de la clase Libro.
"""


class Libro:
    def __init__(self, titulo: str, autores: list, año: int, edicion: str, isbn: int):
        self.titulo = titulo
        self.autores = autores
        self.año = año
        self.edicion = edicion
        self.isbn = isbn

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autores": [
                {"nombre": a.nombre, "apellido": a.apellido} for a in self.autores
            ],
            "año": self.año,
            "edicion": self.edicion,
            "isbn": self.isbn,
        }
