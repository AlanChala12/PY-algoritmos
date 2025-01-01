# Construir una función que reciba como parámetro un entero y un dígito menor o igual a 5 y retorne el dígito del número que se encuentre en la posición especificada por el dígito que llegó como parámetro.

def posicion(numero, digito):
    n = str(numero)

    if 1 <= digito <= len(n): 
        posicion_deseada = digito - 1  
        return f'El dígito en la posición {digito} del número {numero} es {n[posicion_deseada]}.'
    else:
        return f'El dígito {digito} no es una posición válida para el número {numero}.'

try:
    entero = int(input('Ingresa un número entero: '))
    digito = int(input('Ingresa un dígito comprendido en el siguiente rango [1-5]: '))

    if 1 <= digito <= 5:
        print(posicion(entero, digito))
    else:
        print('Por favor, proporciona un dígito comprendido entre 1 y 5.')

except ValueError:
    print('Ingresa valores numéricos.')