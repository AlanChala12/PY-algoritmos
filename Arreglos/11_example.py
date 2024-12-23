# Leer 10 números enteros, almacenarlos en unvector y determinar a cuánto es igual el promedio entero de los datos del vector.
numeros = []
sum_de_digitos = 0
n = 10

for i in range(1, 11):
    numero = int(input(f'Entero {i}: '))
    numeros.append(numero)
    
for x in numeros:
    sum_de_digitos = sum_de_digitos + x 
    
promedio_entero = sum_de_digitos // n
print(f'El promedio entero de {numeros} es de "{promedio_entero}"')