# Construir una función que reciba un entero y le calcule su factorial sabiendo que el factorial de un número es el resultado de multiplicar sucesivamente todos los enteros comprendidos entre 1 y el número dado. El factorialde 0 es 1. No están definidos los factoriales de números negativos.

def factorial_de(entero):
    
    if entero == 0:
        return f'Factorial de {entero}! es: 1'
    
    elif entero < 0:
        return 'El factorial para los número negativos, no está definido'
    
    else:
        facto = entero
        for x in range(1, entero):
            facto = facto * x
        return f'Factorial de {entero}! es: {facto}'

numero = int(input('Ingresa un número entero: '))
print(factorial_de(numero))

    