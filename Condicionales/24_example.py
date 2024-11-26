# Leer un número entero de tres dígitos y determinar cuántos dígitos pares tiene.

x = int(input('Entero: '))

if x < 100:
    print(f'---El número debe ser mayor o igual a cien---')
    
else:
    dig1 = x // 100
    dig2 = (x // 10) % 10
    dig3 = x % 10
    
    #Condiciones
    tres_digitos_pares = dig1 % 2 == 0 and dig2 % 2 == 0 and dig3 % 2 == 0
    dos_digitos_pares = (dig1 % 2 == 0 and dig2 % 2 == 0) or (dig3 % 2 == 0 and dig1 % 2 == 0) or (dig3 % 2 == 0 and dig2 % 2 == 0) 
    un_digito_par = (dig1 % 2 == 0 or dig2 % 2 == 0 or dig3 % 2 == 0)
    
    if tres_digitos_pares == True:
        print(f'--El número {x}, tiene tres dígitos pares--')
        
    elif dos_digitos_pares == True:
        print(f'--El número {x}, tiene dos dígitos pares--')
        
    elif un_digito_par == True:
        print(f'--El número {x}, tiene solo un dígito par--')
        
    else:
        print(f'--El número {x}, no tiene dígitos pares--')
        