# Construir una función que reciba como parámetro un entero y retorne la cantidad de dígitos.

def cantidad_de_digitos(entero):
    
    cantidad_digitos = 0
    
    while entero != 0:
        cantidad_digitos += 1
        entero //= 10
    
    return cantidad_digitos

number = int(input('Ingresa un número entero: '))
digitos = cantidad_de_digitos(number)

print(f'La cantidad de dígitos del número {number} es {digitos}')