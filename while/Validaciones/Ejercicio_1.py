# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

clave = "Messi10"
intentos = 0 
clave = input("Ingrese la clave: ")

while clave != "Messi10":
    intentos += 1
    clave = input("Clave incorrecta. Intente nuevamente: ")
 
else:
    print("Clave correcta. Acceso permitido.")