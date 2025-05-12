# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

num_1 = float(input("Introduce el primer número: "))
num_2 = float(input("Introduce el segundo número: "))
num_3 = float(input("Introduce el tercer número: "))

def def_max():
    numero_maximo = num_1
    if num_2 > numero_maximo:
        numero_maximo = num_2
    if num_3 > numero_maximo:
        numero_maximo = num_3
    return numero_maximo

def_max()
print("El número máximo es: ", def_max())