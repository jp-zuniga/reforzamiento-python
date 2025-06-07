"""
Implementación de la ventana principal del sistema.
"""

from typing import Callable

import customtkinter as ctk

from .inputs import Inputs


class BiblioGUI(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.inputs = Inputs()

        self.title("Gestión de Biblioteca")
        self.geometry("800x600")

        self.contenedor = ctk.CTkFrame(self)
        self.contenedor.pack(pady=20, padx=20, fill="both", expand=True)

        self.titulo = ctk.CTkLabel(
            self.contenedor,
            text="Sistema de Gestión de Biblioteca",
        )

        self.titulo.pack(pady=10)

        self.init_botones()

    def init_botones(self) -> None:
        botones: list[tuple[str, Callable]] = [
            ("Agregar Libro", self.agregar),
            ("Mostrar Todos los Libros", self.mostrar),
            ("Buscar Libro por Título o ISBN", self.buscar),
            ("Eliminar Libro por ISBN", self.eliminar),
            ("Salir", self.quit),
        ]

        for text, command in botones:
            btn = ctk.CTkButton(
                self.contenedor,
                text=text,
                command=command,
                width=200,
                height=40,
                corner_radius=8,
            )

            btn.pack(pady=5)

    def agregar(self) -> None:
        self.inputs.agregar_libro()

    def mostrar(self) -> None:
        self.inputs.mostrar_libros()

    def buscar(self) -> None:
        self.inputs.buscar_libro()

    def eliminar(self) -> None:
        self.inputs.eliminar_libro()
