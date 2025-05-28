# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

suma = 0
contador = 0

for i in range(10):
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero
    contador += 1   

promedio = suma / contador

print("La suma de los números es:", suma)
print("El promedio de los números es:", promedio)

# En caso de tener que aclarar que no se ingresaron números:
# if contador > 0:
#     promedio = suma / contador
#     print(f"La suma es: {suma}")
#     print(f"El promedio es: {promedio}")
# else:
#     print("No se ingresaron números.")