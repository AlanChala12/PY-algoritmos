# Registro de productos.
productos = {}

def productosRegistro(a, b, c):
    
    if a in productos:
        print(f'El producto "{a}" ya ha sido registrado')
        
    else:
        producto = {
        'precio': b,
        'cantidad': c
        } 
    
        productos[a] = producto
        print('¡REGISTRO EXITOSO!')

condicion = True

while condicion:
    x = input('''1. Registro de productos
                 2. Salir''')
    
    if x == "1":
        nombreProducto = input('Producto: ')
        valorProducto = float(input('Valor: '))
        cantidadProducto = int(input('Cantidad: '))
        productosRegistro(nombreProducto, valorProducto, cantidadProducto)
        
    if x == "2":
        condicion = False
        
print(productos)