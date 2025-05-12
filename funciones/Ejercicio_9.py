# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

base = float(input("Introduce la base: "))
exponente = float(input("Introduce el exponente: "))

def potencia():
    resultado = base ** exponente
    return resultado

potencia()
print("El resultado de la potencia es: ", potencia())