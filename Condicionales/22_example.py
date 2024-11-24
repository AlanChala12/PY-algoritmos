# Leer un número entero de tres dígitos y determinar si el primer dígito es igual al último.

number = int(input('Número mayor o igual a cien: '))

if number < 100:
    print('--Ingresa un número mayor o igual a cien--')
    
else:
    dig1 = number // 100
    dig3 = number % 10
    
    if dig1 == dig3: 
        print(f'El primer dígito del número {number} es igual al último dígito.') 
    else: 
        print(f'El primer dígito del número {number} no es igual al último dígito.')