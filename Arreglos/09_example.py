# Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se encuentran los números con más de 3 dígitos.

numeros = [ int(input(f'Entero { i + 1 }: ')) for i in range(10) ]
    
for x in numeros:
    if x >= 100:
        print(f'El número {x} se encuentra en el indice {numeros.index(x)}')

print()
print(numeros)