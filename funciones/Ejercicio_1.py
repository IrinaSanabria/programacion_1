# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def numero_entero() -> int:
    numero = input("Por favor, ingresá un número entero: ")
    if numero.isdigit():
        return int(numero)
    else:
        print("El número ingresado no es un entero. Por favor, ingrese un entero.")
        return numero_entero()

numero_ingresado = numero_entero()
print(f"El número ingresado es: {numero_ingresado}") 