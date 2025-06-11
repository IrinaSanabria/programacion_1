clientes = []
productos = []
ventas = []

def cargar_clientes ():
    while True:
        nombre = input("Ingrese nombre del cliente:")
        if nombre == "":
            print("Nombre inválido, por favor ingrese el nombre del cliente.")
        else:
            break
    # while True:
    #         id = []
    #         id = int(input("Ingrese número de identificación del cliente:"))
    #         for i in id:
    #             if id
    while True:
        provincia = input("Ingrese provincia del cliente:")
        if provincia == "":
             print("Provincia inválida, por favor ingrese la provincia del cliente.")
        else:
            break
    cliente = {"Nombre": nombre, "ID": id, "Provincia": provincia}
    clientes.append

def cargar_productos ():
    # while True:
    #     codigo = []
    #     codigo = int(input("Ingrese el código del producto a cargar:"))
    #     for i in codigo:
    descripcion = input("Descripción del producto:")
    while True:
        precio = input("Ingrese el precio del producto agregado:")
        if precio <= 0:
            print("Error al cargar el precio, debe ser mayor a cero.")
        else:
            break
    producto = {"Código": codigo, "Descripción": descripcion, "Precio": precio}
    productos.append

def registro_ventas ():