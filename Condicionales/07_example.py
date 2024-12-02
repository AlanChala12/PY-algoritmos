# Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.
entero = int(input('Entero: '))
condicion = True

if entero < 0:
    print('No es primo además, es un número negativo')
    
else:
    for x in range(2, entero):
        if entero % x == 0:
            condicion = False
            break
        
    if condicion:
        print('Es primo')
    else:
        print('No es primo')