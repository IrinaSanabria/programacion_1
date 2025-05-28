# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

contador = 0
suma = 0

while contador <= 5:
    numero = float(input("Ingrese un número: "))
    suma += numero
    contador += 1

promedio = suma / 5
print("La suma de los números ingresados es:", suma)
print("El promedio de los números ingresados es:", promedio)