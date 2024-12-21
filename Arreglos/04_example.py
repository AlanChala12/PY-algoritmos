# Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se encuentran los números terminados en 4.
enteros = []

for i in range(1, 11):
  numeros = int(input(f'Entero {i}: '))
  enteros.append(numeros)

for x in enteros:
  if x % 10 == 4:
    print(f'El número {x}, se encuentra en el indice {enteros.index(x)}')
    
print(enteros)