"""Crear un programa donde el usuario pueda crear, ver, modificar y eliminar contactos (nombre y teléfono)."""

import os


def clear():
    os.system("cls")


listaContactos = []


def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    numero = int(input("Ingrese el número del contacto: "))

    contactos = [nombre, numero]
    listaContactos.append(contactos)
    clear()
    print("El contacto se registró correctamente!")


def eliminar():
    if len(listaContactos) == 0:
        print("No hay contactos por eliminar.")
        return
    else:
        nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
        for contacto in listaContactos:
            if contacto[0] == nombre:
                listaContactos.remove(contacto)
                print(f"El contacto: '{nombre}' ha sido eliminado con éxito!")
                break
            else:
                print("Contacto no encontrado.")


def imprimir_pantalla():
    if len(listaContactos) == 0:
        print("No hay contactos en la agenda.")
    else:
        print("Lista de contactos:")
        for i, contacto in enumerate(
            listaContactos, start=1
        ):  # contacto es cada elemento de la lista
            print(f"{i}. Contacto: {contacto[0]}, número: {contacto[1]}")


def modificar_contacto():
    if len(listaContactos) == 0:
        print("No hay contactos en la agenda")
    else:
        nombre = input("Ingrese el nombre del contacto que desea modificar: ")
        for contacto in listaContactos:
            if contacto[0] == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del contacto: ")
                nuevo_numero = int(input("Ingrese el nuevo número celular: "))

                contacto[0] = nuevo_nombre
                contacto[1] = nuevo_numero

                print("Contacto modificado con éxito!")
                return


def menu():
    while True:
        print("\n---- Menú de opciones ----")
        print("1. Registrar nuevo contacto")
        print("2. Eliminar contacto")
        print("3. Mostrar lista de contactos")
        print("4. Modificar contacto")
        print("5. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            eliminar()
        elif opcion == 3:
            imprimir_pantalla()
        elif opcion == 4:
            modificar_contacto()
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")
            input("Presione Enter para volver al menú de inicio.")
            clear()


if __name__ == "__main__":
    menu()
