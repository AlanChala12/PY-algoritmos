# Generar todas las tablas de multiplicar del 1 al 10.

""" Tablas de multiplicar con bucle for."""
for x in range(1, 11):
    
    print(f'Tabla del {x}')
    
    for y in range(1, 11):
        
        multi = x * y
        print(f'{x} x {y} = {multi}')
    
    print()

    


'''Tablas de multiplicar con bucle while'''
number = 0

while number < 10:

    number += 1
    table = 0
    print(f'Tabla del {number}')

    while table < 10:
        
        table += 1
        result = number * table
        print(f'{number} x {table} = {result}')

    print()
