# Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.
 
try:
    num1 = int(input('Entero 1: '))
    num2 = int(input('Entero 2: '))

    if len(str( num1 )) == 2 and len(str( num2 )) == 2:
        
        digs = []
        for i in str( num1 ):
            digs.append(int( i ))
            
        for y in str( num2 ):
            digs.append(int( y ))
        
        sumDigs = sum( digs )
        print(f'La suma de dígitos de los números { num1 } y { num2 } es: { sumDigs }')
        
    else:
        print('Ingresa numeros de dos dígitos')
        
except ValueError:
    print('Ingresa valores numéricos')