# Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos.

number = int(input('Entero: '))

if number < 100:
    print('--Ingresa un número mayor o igual a cien--')
    
else:
    dig1 = number // 100
    dig2 = (number // 10) % 10
    dig3 = number % 10
    
    result = dig1 + dig2 + dig3
    print(f'La suma de los dígitos del número {number}, es de {result}')