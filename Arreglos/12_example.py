# Leer 10 números enteros, almacenarlos en un vector y determinar si el promedio entero de estos datos está almacenado en el vector.

numeros = []
sum_de_digitos = 0
n = 10

for i in range(1, 11):
    numero = int(input(f'Entero {i}: '))
    numeros.append(numero)
    
for x in numeros:
    sum_de_digitos = sum_de_digitos + x 
    
promedio_entero = sum_de_digitos // n

if promedio_entero in numeros:
    print(f'El promedio entero "{promedio_entero}" se encuentra en el vector {numeros}')
else:
    print(f'El promedio entero "{promedio_entero}" no se encuentra en el vector {numeros}')
    