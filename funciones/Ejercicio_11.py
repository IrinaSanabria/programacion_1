# Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. 
# La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

number = int(input("Por favor, ingrese un número: "))
contador_primos = 0

def cantidad_numeros_primo():
    if number <= 1:
        print(f"El número {number} no es primo")
    else:
        es_primo = True
        for i in range(2, number):
            if numero % i == 0:
            es_primo = False
            break
        if es_primo:
            print(f"El número {number} es primo")
        else:
            print(f"El número {number} no es primo")