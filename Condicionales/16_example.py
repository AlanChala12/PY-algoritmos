# Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos.
number = int(input('Ingresa un número entero mayor o igual a 100: '))

print()

if number >= 100:
    
    x = number // 10
    dig1 = x // 10
    dig2 = x % 10
    dig3 = number % 10
    result = dig1 + dig2 + dig3
    
    print(f'La suma de los dígitos del número {number}, es de: {result}')
    
else:
    
    print('--El número proporcionado es muy pequeño--')
    