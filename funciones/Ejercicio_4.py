# Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

def area_rectangulo():
    """
    Calcula el área de un rectángulo.

    Parámetros:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    area = base * altura
    return area

area_rectangulo()
print(f"El área del rectángulo es: {area_rectangulo()}")