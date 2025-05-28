# Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

while True:
    color = input("Ingrese un color: ")
    if color == "Rojo" or color == "Verde" or color == "Azul" or color == "rojo" or color == "verde" or color == "azul":
        print("Color válido. Muchas gracias.")
        break
    else:
        print("Color inválido. Intente nuevamente: ")