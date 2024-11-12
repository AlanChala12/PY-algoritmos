# Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.

number = int(input('Ingresa un número entero: '))

if number < 10:
    print('--Ingresa un número entero mayor o igual que 10--')

elif number >= 10 and number < 99:
    
    dig1 = int(number / 10)
    
    dig2 = int(number / 10) * 10
    dig2 = number - dig2
    
    if dig1 > dig2:
        
        for intervalo1 in range(dig2, dig1, 1):
            print(intervalo1)
            
    elif dig2 > dig1:
        
        for intervalo2 in range(dig1, dig2, 1):
            print(intervalo2)
        
    else:
        print(f'--Los dígitos que conforman al número {number}, son iguales, por lo tanto no hay intervalo que mostrar--')