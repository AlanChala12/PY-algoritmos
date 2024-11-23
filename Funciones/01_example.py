# Construir una función que reciba como parámetro un entero y retorne sus dos últimos dígitos.

def ultimos_digitos(entero):
    
    if entero < 10:
        return entero
    
    elif entero <= 99:
        return entero % 10
    
    else:
        return entero % 100
    
number = int(input('Ingresa un número entero: '))
digitos = ultimos_digitos(number)

print(f'Los últimos dígitos del número {number} son {digitos}')

