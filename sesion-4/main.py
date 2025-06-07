"""
Crea un programa que simule un sistema básico de gestión de una biblioteca. El programa debe permitir:
- Agregar libros (título, autor, año, ISBN).
- Mostrar todos los libros registrados.
- Buscar un libro por título o ISBN.
- Eliminar un libro por ISBN.
- Salir del programa.
"""

from gestion_biblio import views


def main():
    instancia = views.BiblioGUI()
    instancia.mainloop()


if __name__ == "__main__":
    main()
