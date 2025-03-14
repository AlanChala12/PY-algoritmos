# Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.
w = int(input('Primer entero: '))
z = int(input('Segundo entero: '))

menor = min(w, z)
mayor = max(w, z)

if mayor == menor:
    print('Los números proporcionados son iguales: ')
    
else:
    for x in range(menor, mayor + 1):
        if x % 10 == 4:
            print(x)