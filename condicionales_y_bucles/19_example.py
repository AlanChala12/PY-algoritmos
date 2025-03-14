# Leer un número entero y determinar si es primo
entero = int(input('Entero: '))
es_primo = True

for x in range(2, entero):
    if entero % x == 0:
        es_primo = False
        break

if es_primo and entero > 1:
    print('Es primo')
else:
    print('No es primo')
