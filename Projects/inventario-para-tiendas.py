productos = {}

def registrar_producto(nombre, valor, cantidad):
    if nombre in productos:
        print('El producto ya ha sido registrado')
    else:
        producto = {
        'valor': valor,
        'cantidad': cantidad
        }
        
    productos[nombre] = producto
    
def registrar_compra(nombre, cantidad):
    if nombre in productos:
        
        if cantidad > productos[nombre]['cantidad']:
            print('!Los productos son insuficientes¡')
        else:
            productos[nombre]['cantidad'] -= cantidad 
    else:
        print(f'El producto "{nombre}", no se encuentra en la base de datos.')
        