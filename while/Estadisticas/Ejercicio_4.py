# Mostrar la suma de los números pares desde el 1 hasta el 10.

contador = 1
suma = 0

while contador <= 10:
    if contador % 2 == 0:
        suma += contador
    contador += 1
    print(suma)
print("La suma de los números pares desde el 1 hasta el 10 es:", suma)