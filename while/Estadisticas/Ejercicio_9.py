# Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

contador = 0
suma = 0

while contador < 5:
    numero_ingresado = int(input("Ingrese un número: "))
    contador += 1
    suma += numero_ingresado

promedio = suma / contador
print(f"La suma de los números ingresados es: {suma}")
print(f"El promedio de los números ingresados es: {promedio}")

# contador = 0
# suma = 0
# continuar = True

# numero_ingresado = int(input("Ingrese la cantidad de números que desee (mínimo 5, ingrese 0 para finalizar): "))

# while continuar:
#     numero_ingresado = int(input("Ingrese la cantidad de números que desee (mínimo 5, ingrese 0 para finalizar): "))
#     contador += 1
#     suma += numero_ingresado
#     if numero_ingresado == 0:
#         continuar = False

# print(f"La suma de los números ingresados es: {suma}")
# print(f"El promedio de los números ingresados es: {suma / contador}")