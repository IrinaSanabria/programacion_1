# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

producto_negativos = 1 
suma = 0
respuesta = input("¿Desea ingresar números? (s/n): ")

while respuesta == "s":
    numero = float(input("Ingrese un número: "))
    if numero > 0:
        suma += numero
    elif numero < 0:
        producto_negativos *= numero
        contador_negativos += 1

respuesta = input("¿Desea ingresar otro número? (s/n): ")

print("La suma de los números positivos es:", suma)
print("El producto de los números negativos es:", producto_negativos)