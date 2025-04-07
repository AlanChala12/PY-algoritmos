# Leer 10 números enteros, almacenarlos en un vector y determinar cuáles son los datos almacenados múltiplos de 3.

numeros = [ int(input(f'Entero { i + 1 }: ')) for i in range( 10 ) ]
    
print()    
print(f'Los múltiplos de 3 que están en el vector {numeros} son')   

for z in numeros:
    if z % 3 == 0:
        print(z)

