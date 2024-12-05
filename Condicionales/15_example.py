# Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.
 
x = int(input('Ingresa un número entero positivo mayor o igual a diez: '))
y = int(input('Ingresa otro número entero positivo mayor o igual a diez: '))

print()

if 10 <= x < 100 and 10 <= y < 100:
    
    dig1_x = x // 10
    dig2_x = x % 10
    
    dig1_y = y // 10
    dig2_y = y % 10
    
    result = dig1_x + dig2_x + dig1_y + dig2_y
    
    print(f'La suma de los dígitos de los números {x} y {y}, es de: {result}')
        
else:
    
    print('¡ERROR! Ambos números deben cumplir la condición solicitada.')
    
