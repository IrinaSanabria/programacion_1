# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

number = int(input("Por favor, ingrese un número: "))

def definir_numero_primo() -> bool:
    if number <= 1:
        return False
    else:
        for i in range(1, number):
            if number % i == 0:
                return True
            else:
                return False

definir_numero_primo()
print(f"El número {number} es primo = {definir_numero_primo()}")