number = int(input('Ingresa un número entero: '))

if number < 10:
    print(f'La suma de {number} es: {number}')
    
elif number >= 10 and number < 100:
    
    dig1 = int(number / 10)
    dig2 = int(number / 10) * 10
    dig2 = number - dig2
    
    result = dig1 + dig2
    print(f'La suma de los dígitos del número {number} es: {result}')