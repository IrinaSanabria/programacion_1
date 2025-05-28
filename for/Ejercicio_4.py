# Ingresar un número y mostrar la tabla de multiplicar de ese número.

numero_ingresado = int(input("Ingrese un número: "))

for i in range(1, 11):
    print(numero_ingresado, "x", i, "=", numero_ingresado * i)