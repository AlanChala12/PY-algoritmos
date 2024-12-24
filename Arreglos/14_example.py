# Leer 10 números enteros, almacenarlos en un vector y determinar cuántos datos almacenados son múltiplos de 3.

numeros = []
multiplos_de_tres = 0

for i in range(1, 11):
    numero = int(input(f'Entero {i}: '))
    numeros.append(numero)
    
for z in numeros:
    if z % 3 == 0:
        multiplos_de_tres += 1

print(f'La cantidad de dígitos, que son múltiplos de tres, son: {multiplos_de_tres}')