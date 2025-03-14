# Leer dos números y mostrar todos los enteros comprendidos entre ellos.
x = int(input('Ingresa un entero: '))
y = int(input('Ingresa otro entero: '))

menor = min(x, y)
mayor = max(x, y)

if menor == mayor:
    print('---Los números proporcionados, son iguales---')

else:
    print(f'---Los enteros comprendidos entre {menor} y {mayor}, son---')
    for z in range(menor, mayor, 1):
        print(z)