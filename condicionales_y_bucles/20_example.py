# Leer un número entero y determinar si la suma de sus dígitos es también un número primo.
entero = int(input('Entero: '))
cantidad_digitos = []
es_primo = True
suma_de_digitos = 0

while entero != 0:
    digitos = entero % 10
    cantidad_digitos.append(digitos)
    entero //= 10
    
for i in cantidad_digitos:
    suma_de_digitos = suma_de_digitos + i
    
for x in range(2, suma_de_digitos):
    if suma_de_digitos % x == 0:
        es_primo = False
        break

if es_primo:
    print('Es primo')
else:
    print('No es primo')