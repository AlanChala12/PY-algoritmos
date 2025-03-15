# Sin usar ningún método de string, imprimir lo siguiente "123...n"

n = int(input('Entero: '))
numbers = ''

for i in range(1, n + 1):
    numbers += f'{i}'

print( numbers )