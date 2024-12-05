# Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes.

number1 = int(input('Ingresa un número entero mayor o igual que diez: '))
number2 = int(input('Ingresa otro número entero mayor o igual a diez: '))

print()

if number1 < 10 and number2 < 10:
    print('--Ambos números deben ser mayor o igual a diez--')
    
else:
    
    dig1_number1 = number1 // 10
    dig2_number1 = number1 % 10
    
    dig1_number2 = number2 // 10
    dig2_number2 = number2 % 10
    
    if dig1_number1 == dig1_number2 or dig1_number1 == dig2_number2 or dig2_number1 == dig2_number2 or dig2_number1 == dig2_number2:
        print(f'Los números {number1} y {number2}, tienen dígitos comúnes.')
        
    else:
        print(f'Los números {number1} y {number2}, no tienen dígitos comúnes.')
        