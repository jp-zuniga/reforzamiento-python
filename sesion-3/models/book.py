class Book:
    def __init__(self, titulo: str, autores: list, anio: int, edicion: str, isbn: int):
        self.titulo = titulo
        self.autores = autores
        self.anio = anio
        self.edicion = edicion 
        self.isbn = isbn
        
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autores": [{"nombre": a.nombre, "apellido": a.apellido} for a in self.autores],
            "anio": self.anio,
            "edicion": self.edicion,
            "isbn": self.isbn
        }