# Construir una función que reciba como parámetro un entero y retorne la cantidad de dígitos pares.

def cantidad_digitos_pares(entero):
    cantidad_digitos = 0
    
    while entero != 0:
        
        y = entero % 10
        entero //= 10
    
        if y % 2 == 0:
            cantidad_digitos += 1
    
    return cantidad_digitos

number = int(input('Ingresa un número entero: '))
result = cantidad_digitos_pares(number)

print(f'La cantidad de dígitos pares del número {number} es {result}')
