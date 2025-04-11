# Leer 10 números enteros, almacenarlos en un vector y determinar cuáles son los números múltiplos de 5 y en qué posiciones están

try:
    enteros = [ int(input(f'Entero { x + 1 }: ')) for x in range( 10 ) ]
    print('--Múltiplos de cinco--')
    
    for i, num in enumerate( enteros ):
        if num % 5 == 0:
            print(f'Valor: { num } - Posición: { i + 1 }')
    
except ValueError:
    print('Ingresa valores numéricos')
