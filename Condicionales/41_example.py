# Leer dos números enteros y determinar si la diferencia entre los dos es un número divisor exacto de alguno de los dos números.

entero1 = int(input('Ingresa el primer número entero: '))
entero2 = int(input('Ingresa el segundo número entero: '))

diferencia = abs(entero1 - entero2)

if diferencia == 0:
    print('Ambos números son iguales, no hay diferencia.')

elif entero1 % diferencia == 0:
    print(f'La diferencia entre {entero1} y {entero2} es divisor exacto de {entero1}.')

elif entero2 % diferencia == 0:
    print(f'La diferencia entre {entero1} y {entero2} es divisor exacto de {entero2}.')
    
else:
    print(f'La diferencia entre {entero1} y {entero2} no es divisor de ninguno de los números proporcionados.')