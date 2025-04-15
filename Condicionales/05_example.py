# Leer un número entero y determinar a cuánto es igual la suma de sus dígitos.

try:
    num = int(input('Entero: '))
    digs = []

    for i in str(num):
        digs.append( int(i) )
        
    sumDigs = sum( digs )
    print(f'La suma de dígitos del número { num } es { sumDigs }')
    
except ValueError:
    print('Ingresa valores numéricos')