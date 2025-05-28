# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

contador = 0
suma = 0
respuesta = input("¿Desea ingresar números? (s/n): ")

while respuesta == "s":
    numero = float(input("Ingrese un número: "))
    suma += numero
    contador += 1
    respuesta = input("¿Desea ingresar otro número? (s/n): ")

promedio = suma / contador
print("La suma de los números ingresados es:", suma)
print("El promedio de los números ingresados es:", promedio)