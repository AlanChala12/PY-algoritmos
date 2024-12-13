# Leer un número entero, si es múltiplo de 4, mostrar en pantalla su mitad; si es múltiplo de 5, mostrar en pantalla su cuadrado, si es múltiplo de 6, mostrar en pantalla su primer dígito. Asumir que el número no es mayor que 100.

entero = int(input('Entero: '))

if entero % 4 == 0:
    mitad_entero = entero // 2
    print(f'La mitad del número {entero} es: {mitad_entero}')

elif entero % 5 == 0:
    print(entero ** 2)

elif entero % 6 == 0:
    if entero < 10:
        print(entero)
    
    elif 10 <= entero < 100:
        print(entero // 10)
        
    elif 100 <= entero < 1000:
        print(entero // 100)
        
    else:
        print(f'El número {entero} es múltiplo de 6 pero contiene 4 dígitos')

else:
    print('¡Hola!')
