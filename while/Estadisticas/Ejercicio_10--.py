# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

contador = 0
suma = 0

numero_ingresado = int(input("Ingrese un número: "))

while contador > 5 or contador < 10:
    numero_ingresado = int(input("Ingrese un número: "))
    suma += numero_ingresado
    contador += 1

print(f"La suma de los números ingresados es {suma}")
print(f"El promedio de los números ingresados es {suma / contador}")