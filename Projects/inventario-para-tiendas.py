# Registro de productos.
cantidad_de_productos = int(input('¿Cuantos productos deseas registrar el día de hoy?: '))
productos = {}

for xx in range(0, cantidad_de_productos):

    nombre = input("Nombre del producto: ").lower()
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Ingresa la cantidad disponible del producto: "))

    productos[nombre] = {
        'precio': precio,
        'cantidad': cantidad,
    }

print(f'Los productos regristrados son: {productos}')
print()


#Gestión de existencias
def comprar_producto(nombre_producto, cantidad):

    if nombre_producto in productos:
        producto = productos[nombre_producto]
        
        if producto["cantidad"] >= cantidad:
            producto["cantidad"] -= cantidad

        else:
            print(f"No hay suficiente stock de {nombre_producto}. Quedan {producto['cantidad']} disponibles.")

    else:
        print(f"El producto '{nombre_producto}' no está registrado.")


nombre_producto = input("Ingrese el nombre del producto que desea comprar: ").lower()
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

# Realizar la compra
comprar_producto(nombre_producto, cantidad)