# Leer dos números enteros y determinar si la suma de los dos números origina un número par.
number1 = int(input('Ingresa un número entero positivo: '))
number2 = int(input('Ingresa otro número entero positivo: '))

resultado = number1 + number2

if resultado % 2 == 0:
    print(f'El resultado de la suma de {number1} y {number2} da como resultado un número par.')
    
else:
    print(f'El resultado de la suma de {number1} y {number2} no da como resultado un número par.')