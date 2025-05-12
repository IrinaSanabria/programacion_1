# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

contador_numeros = 0
maximo = 0
minimo = 10000000000

while contador_numeros < 10:
    numero = int(input("Por favor, ingresar un número entero: "))
    contador_numeros += 1
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero 

print(f"El número máximo es: {maximo}")
print(f"El número mínimo es: {minimo}")

# contador_numeros = 0
# numero = int(input("Por favor, ingresar un número entero: "))

# maximo = numero
# minimo = numero

# while contador_numeros < 10:
#     numero = int(input("Por favor, ingresar un número entero: "))
    
#     if numero > maximo:
#         maximo = numero
#     if numero < minimo:
#         minimo = numero

#     contador_numeros += 1

# print(f"El número máximo es: {maximo}")
# print(f"El número mínimo es: {minimo}")