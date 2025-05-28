# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

# El área de un círculo se calcula con la fórmula: A = π * r^2, donde r es el radio y π es una constante aproximadamente igual a 3.14159.

radio = float(input("Ingrese el radio del círculo: "))

def area_circulo():
    """
    Calcula el área de un círculo.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    pi = 3.14159
    area = pi * (radio ** 2)
    return area

area_circulo()
print(f"El área del círculo es: {area_circulo()}")