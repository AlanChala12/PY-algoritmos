# Leer un número entero de dos dígitos y determinar si un dígito es múltiplo del otro.

number = int(input('Ingresa un número entero que contenga dos dígitos: '))

dig1 = number // 10
dig2 = number % 10 

if number < 10 or number >= 100:
    print('--Debe ser un número mayor o igual que 10 y menor que 100--')

elif dig1 % dig2 == 0:
    print(f'--El número {dig2} es múltiplo de {dig1}.')

elif dig2 % dig1 == 0:
    print(f'--El número {dig1} es múltiplo de {dig2}.')

else:
    print('--Ningún número es múltiplo del otro--')
    
    