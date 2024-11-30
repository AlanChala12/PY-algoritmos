# Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.
x = int(input('Ingresa un número: '))

print('--Múltiplos del número cinco--')
for y in range(1, x + 1):
    
    if y % 5 == 0:
        print(y)
        