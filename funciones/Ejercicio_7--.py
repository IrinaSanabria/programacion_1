# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def par_o_impar():
    numero = int(input("Por favor ingrese un número: "))
    if numero % 2 == 0:
        return True
    else:
        return False
    if True:
        print("El número es par.")
    else:
        print("El número es impar.")

par_o_impar()