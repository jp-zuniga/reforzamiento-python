"""
Implementación de la clase Inputs, la cual se encarga de
pedir y validar las entradas del usuario. A la hora de
registrar estas entradas, se cuenta con la clase Biblioteca.
"""

from tkinter import messagebox
from typing import Optional

import customtkinter as ctk

from ..models import Libro
from ..services import Biblioteca


class Inputs:
    def __init__(self) -> None:
        self.biblio = Biblioteca()
        self.ventana_actual: Optional[ctk.CTkToplevel] = None

    def _cerrar_ventana(self) -> None:
        """
        Cerrar ventana si existe.
        """

        # si self.ventana_actual contiene una instancia
        # de CTkToplevel y esa instancia existe, eliminarla
        if self.ventana_actual is not None and self.ventana_actual.winfo_exists():
            self.ventana_actual.destroy()

    def _setup_ventana(self, titulo: str, dimensiones: str) -> ctk.CTkToplevel:
        """
        Maneja la creación de una nueva ventana.
        """

        self._cerrar_ventana()
        self.ventana_actual = ctk.CTkToplevel()
        self.ventana_actual.title(titulo)
        self.ventana_actual.geometry(dimensiones)
        return self.ventana_actual

    def _crear_boton(self, parent, texto: str, comando) -> ctk.CTkButton:
        """
        Maneja la creación de botones.
        """

        return ctk.CTkButton(
            parent,
            text=texto,
            command=comando,
        )

    def _crear_campo_input(self, parent, label_text: str) -> ctk.CTkEntry:
        """
        Maneja la creación del CTkLabel y CTkEntry de un campo.
        """

        ctk.CTkLabel(parent, text=label_text).pack()
        entry = ctk.CTkEntry(parent)
        entry.pack(pady=5)
        return entry

    def _validar_input(
        self, valor: str, nombre_campo: str, es_numerico: bool = False
    ) -> bool:
        """
        Maneja la validación de inputs, y se encarga
        de mostrar mensajes de error si es necesario.
        """

        if not valor:
            messagebox.showerror("Error", f"El campo {nombre_campo} es requerido.")
            return False
        if es_numerico and not valor.isdigit():
            messagebox.showerror("Error", f"{nombre_campo} debe ser numérico.")
            return False
        return True

    def agregar_libro(self) -> None:
        """
        Crea la interfaz para agregar un libro nuevo al registro.
        """

        ventana = self._setup_ventana("Agregar Libro", "500x400")
        ctk.CTkLabel(ventana, text="Agregar Nuevo Libro", font=ctk.CTkFont(size=16)).pack(
            pady=10
        )

        titulo_entry = self._crear_campo_input(ventana, "Título del libro:")
        autor_entry = self._crear_campo_input(ventana, "Autor:")
        año_entry = self._crear_campo_input(ventana, "Año de publicación:")
        isbn_entry = self._crear_campo_input(ventana, "ISBN:")

        def obtener_input() -> None:
            """
            Obtiene los valores ingresados a los CTkEntry's,
            y si son validos, crea un nuevo Libro y lo agrega.
            """

            # todas los inputs tienen que ser validos
            if not all(
                [
                    self._validar_input(titulo_entry.get(), "título"),
                    self._validar_input(autor_entry.get(), "autor"),
                    self._validar_input(año_entry.get(), "año", es_numerico=True),
                    self._validar_input(isbn_entry.get(), "ISBN"),
                ]
            ):
                return

            if self.biblio.agregar_libro(
                Libro(
                    titulo=titulo_entry.get(),
                    autor=autor_entry.get(),
                    año=int(año_entry.get()),
                    isbn=isbn_entry.get(),
                )
            ):
                messagebox.showinfo("Éxito", "Libro agregado exitosamente.")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo agregar el libro.")

        self._crear_boton(ventana, "Agregar Libro", obtener_input).pack(pady=20)

    def mostrar_libros(self) -> None:
        """
        Crea la interfaz para mostrar todos los libros registrados.
        """

        libros_str = self.biblio.mostrar_libros()

        ventana = self._setup_ventana("Todos los Libros", "800x600")
        ctk.CTkLabel(ventana, text="Listado de Todos los Libros").pack(pady=10)

        registro_textbox = ctk.CTkTextbox(
            ventana,
            width=700,
            height=400,
        )

        registro_textbox.insert(
            "end", libros_str if libros_str else "No hay libros registrados"
        )

        registro_textbox.configure(state="disabled")
        registro_textbox.pack(pady=10, padx=10)

    def buscar_libro(self) -> None:
        """
        Crea la interfaz para buscar un libro por título o ISBN.
        """

        ventana = self._setup_ventana("Buscar Libro", "600x400")
        ctk.CTkLabel(ventana, text="Buscar Libro", font=ctk.CTkFont(size=16)).pack(
            pady=10
        )

        busqueda_entry = self._crear_campo_input(ventana, "Ingrese título o ISBN:")
        resultado_textbox = ctk.CTkTextbox(ventana, width=450, height=250)
        resultado_textbox.pack(pady=10)
        resultado_textbox.configure(state="disabled")

        def buscar() -> None:
            """
            Ejecuta la búsqueda con el input del usuario y muestra el resultado.
            """

            busqueda = busqueda_entry.get()
            if not self._validar_input(busqueda, "término de búsqueda"):
                return

            resultado = self.biblio.buscar_libro(busqueda)
            resultado_textbox.configure(state="normal")
            resultado_textbox.delete("1.0", "end")
            resultado_textbox.insert(
                "end", resultado if resultado else "No se encontraron resultados"
            )

            resultado_textbox.configure(state="disabled")

        self._crear_boton(ventana, "Buscar", buscar).pack(pady=10)

    def eliminar_libro(self) -> None:
        """
        Crea la interfaz para eliminar un libro por título o ISBN.
        """

        ventana = self._setup_ventana("Eliminar Libro", "600x400")
        ctk.CTkLabel(ventana, text="Eliminar Libro", font=ctk.CTkFont(size=16)).pack(
            pady=10
        )

        busqueda_entry = self._crear_campo_input(
            ventana, "Ingrese título o ISBN del libro:"
        )

        def confirmar() -> None:
            """
            Pide confirmación antes de ejecutar la eliminación con el input del usuario.
            """

            busqueda = busqueda_entry.get()
            if not self._validar_input(busqueda, "título o ISBN"):
                return

            if not messagebox.askyesno(
                "Confirmar", "¿Está seguro que desea eliminar este libro?"
            ):
                return

            if self.biblio.eliminar_libro(busqueda):
                messagebox.showinfo("Éxito", "Libro eliminado correctamente")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se encontró el libro")

        self._crear_boton(ventana, "Eliminar", confirmar).pack(pady=20)
