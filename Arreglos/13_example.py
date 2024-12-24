# Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces se repite el promedio entero de los datos dentro del vector.

numeros = []
sum_de_digitos = 0
n = 10
contador = 0

for i in range(1, 11):
    numero = int(input(f'Entero {i}: '))
    numeros.append(numero)
    
for x in numeros:
    sum_de_digitos = sum_de_digitos + x 
    
promedio_entero = sum_de_digitos // n

for z in numeros:
    if promedio_entero == z:
        contador += 1
        
print(f'El promedio entero de los datos {promedio_entero}, se repite {contador} vez/veces')