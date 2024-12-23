# Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números tienen, de los almacenados allí, menos de 3 dígitos.
numeros = []
contador = 0

for i in range(1, 11):
    numero = int(input(f'Entero {i}: '))
    numeros.append(numero)
    
for x in numeros:
    if x < 100:
        contador += 1
        
print(f'Los números almacenados que tienen menos de 3 dígitos, son {contador}.')
print(numeros)