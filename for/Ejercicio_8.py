# Realizar un programa que permita mostrar una pirámide de números.

number = int(input("Ingrese un número: "))

for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()