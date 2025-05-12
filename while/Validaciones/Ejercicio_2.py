# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

clave = "4321"
intentos = 0

clave = input("Ingrese la clave: ")
while clave != "4321" and intentos < 2:
    intentos += 1
    clave = input("Clave incorrecta. Intente nuevamente: ")
    if clave == "4321":
        print("Clave correcta. Acceso permitido.")
        break
    if intentos == 2:
        print("Clave incorrecta, demasiados intentos. Acceso denegado.")