"""
Representar las notas de todas las clases de un grupo de estudiantes con matrices.
Calcular los promedios de cada estudiante y de cada clase.
"""


def crear_notas() -> list[list[float]]:
    try:
        num_clases = int(input("Ingresar el numero de clases: "))
        num_estudiantes = int(input("Ingresar el numero de estudiantes: "))
    except TypeError:
        input("Error: tipo de dato inesperado. Debe ingresar un numero entero.")
        return crear_notas()

    notas = []
    for i in range(num_clases):
        fila = []
        for j in range(num_estudiantes):
            fila.append(0.0)
        notas.append(fila)

    return notas


def ingresar_notas(notas: list[list[float]]) -> list[list[float]]:
    i = 0
    while i < len(notas):
        j = 0
        while j < len(notas[i]):
            try:
                notas[i][j] = float(input(f"Ingrese la nota del estudiante {j + 1}: "))
                j += 1
            except TypeError:
                input("Debe ingresar un float!")
        i += 1

    return notas


def mostrar_notas(notas: list[list[float]]) -> None:
    print("Notas de estudiantes:")
    print("----------------------------------------\n")
    for i in range(len(notas)):
        print(f"Notas de clase {i + 1}:")
        print("--------------------------")
        for j in range(len(notas[i])):
            print(f"Nota de estudiante {j + 1}: {notas[i][j]}")

    input("Presione Enter para continuar...")


def calcular_promedio_por_clase(notas: list[list[float]]) -> list[float]:
    promedios_clase: list[float] = []

    for i in range(len(notas)):
        suma_notas = 0.0
        for j in range(len(notas[i])):
            suma_notas += notas[i][j]
        promedios_clase.append(suma_notas / len(notas[i]))

    return promedios_clase


def calcular_promedio_por_estudiante(notas: list[list[float]]) -> list[float]:
    promedio_estudiantes: list[float] = []

    for j in range(len(notas[0])):
        suma_notas = 0.0
        for i in range(len(notas)):
            suma_notas += notas[i][j]
        promedio_estudiantes.append(suma_notas / len(notas))

    return promedio_estudiantes


def main() -> None:
    notas = crear_notas()
    notas = ingresar_notas(notas)

    promedios_clase = calcular_promedio_por_clase(notas)
    promedios_estudiantes = calcular_promedio_por_estudiante(notas)

    print("\nPromedio de cada clase:")
    print("----------------------------------------\n")
    for i in range(len(notas)):
        print(f"Promedio de clase {i + 1}: {promedios_clase[i]}")

    print("\nPromedio de cada estudiante:")
    print("----------------------------------------\n")
    for j in range(len(notas)):
        print(f"Promedio de estudiante {i + 1}: {promedios_estudiantes[j]}")

    input("\nPresione Enter para salir...")


if __name__ == "__main__":
    main()
