# Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

while True:
    nota = int(input("Ingrese una nota: "))
    if nota > 0 and nota < 11:
        print(f"Nota ingresada: {nota}")
    else:
        print("La nota no es válida.")
        break