#Leer un número entero de tres dígitos y determinar si al menos dos de sus tres dígitos son iguales.
number = int(input('Ingresa un número entero mayor o igual a cien: '))

print()

if number >= 100:
    x = number // 10
    
    dig1 = x // 10
    dig2 = x % 10
    dig3 = number % 10
    
    result = dig1 + dig2 + dig3
    
    if dig1 == dig2 and dig1 == dig3 and dig2 == dig3:
        print(f'Todos los dígitos del número {number}, son iguales.')
        
    elif dig1 == dig2 or dig1 == dig3 or dig2 == dig3:
        print(f'Solo dos dígitos del número {number}, son iguales.')
        
    else:
        print(f'--El número proporcionado no posee dígitos iguales--')
    
else:
    print('--El número proporcionado es muy pequeño--')