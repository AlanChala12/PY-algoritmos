# Leer 10 números enteros, almacenarlos en un vector y determinar cuáles son los números múltiplos de 5 y en qué posiciones están.

enteros = []
multiplos = []

for i in range(1, 11):
    numeros = int(input(f'Entero {i}: '))
    enteros.append(numeros)

print('Los múltiplos de 5 son:')
print('Valor / Índice')
print()

for indice, valor in enumerate(enteros):
    if valor % 5 == 0:
        multiplos.append(valor)
        print(f'{valor} = {indice}')

if not multiplos: 
    print('No se encontraron múltiplos de 5.')

print(f'\nVector de enteros: {enteros}')