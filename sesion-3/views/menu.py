from .inputs import Inputs
import os


def menu():
    inputs: Inputs = Inputs()
    while True:
        print("=== Sistema de Gestion de Biblioteca ===")
        print("1. Agregar Libro")
        print("2. Mostrar Todos los Libros")
        print("3. Buscar Libro por Titulo o ISBN")
        print("4. Eliminar Libro por ISBN")
        print("5. Salir")
        opc = input("Selecione una opcion: ")
        match opc:
            case "1":
                inputs.case_one()
                os.system("pause")
            case "2":
                inputs.case_two()
                os.system("pause")
            case "3":
                inputs.case_three()
                os.system("pause")
            case "4":
                inputs.case_four()
                os.system("pause")
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida...")
