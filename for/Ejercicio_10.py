# Ingresar un número. Determinar si el número es primo o no.

numero = int(input("Ingrese un número: "))

if numero <= 1:
    print("No es primo")
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")