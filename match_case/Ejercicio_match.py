# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# a.Si es invierno: solo se viaja a Bariloche.
# b.Si es verano: se viaja a Mar del plata y Cataratas.
# c.Si es otoño: se viaja a todos los lugares.
# d.Si es primavera: se viaja a todos los lugares menos Bariloche.

estacion = input("Ingrese la estación del año en la que querría viajar: ")
zona = input("Ingrese el lugar al que le gustaría viajar: ")

match estacion:
    case "invierno":
        if zona == "Bariloche" or zona == "bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case "verano":
        if zona == "Mar del plata" or zona == "Cataratas" or zona == "mar del plata" or zona == "cataratas":
            print("Se viaja")
        else:
            print("No se viaja")
    case "otoño":
        print("Se viaja")
    case "primavera":
        if zona == "Bariloche":
            print("No se viaja")
        else:
            print("Se viaja")
    case _:
        print("La estación ingresada no es válida. Por favor, ingrese una estación válida (invierno, verano, otoño, primavera).") 