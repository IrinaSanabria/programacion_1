from funciones import *

def menu():
    matriz = []  # Inicializamos la matriz vacía
    while True:
        print("\n--- MENÚ ---")
        print("1. Cargar matriz de notas")
        print("2. Mostrar porcentaje de aprobados por alumno")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                n = int(input("Ingrese la cantidad de alumnos: "))
                m = int(input("Ingrese la cantidad de exámenes: "))
                matriz = cargar_matriz_notas(n, m)
            case "2":
                if matriz:
                    porcentaje_aprobados(matriz)
                else:
                    print("Debe cargar la matriz primero.")
            case "3":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

menu() # Llamado a la función