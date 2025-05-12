# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

cantidad_divisores = 0
numero = int(input("Ingrese un número: "))

for i in range (1, numero + 1):
    if numero % i == 0:
        print(i)
        cantidad_divisores += 1
print("La cantidad de divisores encontrados es:", cantidad_divisores)