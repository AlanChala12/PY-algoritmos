# Leer dos números enteros y determinarsi la diferencia entre los dos es un número par.
number1 = int(input('Primer entero: '))
number2 = int(input('Segundo entero: '))

diferencia = abs(number1 - number2)

if diferencia % 2 == 0:
    print(f'La diferencia entre los números {number1} y {number2} da como resultado un número ¡par!')
    
else:
    print(f'La diferencia entre los números {number1} y {number2} no da como resultado un número ¡par!')
    