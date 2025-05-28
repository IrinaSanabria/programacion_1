# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def palabra() -> str:
    cadena = str(input("Por favor, ingresá una palabra: "))
    if cadena.isalpha():
        return cadena
    else:
        print("El valor ingresado no es una palabra. Por favor, ingrese una palabra.")
        return palabra()

palabra_ingresada = palabra()
print(f"La palabra ingresada es: {palabra_ingresada}") 