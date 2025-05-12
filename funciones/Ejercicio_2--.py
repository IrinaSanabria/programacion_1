# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def numero_flotante() -> float:
    numero = input("Por favor, ingresá un número flotante: ")
    if numero.isdigit():
        numero = float(numero)
        return numero
    else:
        print("El valor ingresado no es un número flotante válido.")
        return numero_flotante()

numero_ingresado = numero_flotante()
print(f"El número ingresado es: {numero_ingresado}") 