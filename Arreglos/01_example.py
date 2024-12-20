# Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número par leído.
enteros = []
numeros_pares = []

for i in range(1, 11):
  numero = int(input(f'Entero {i}: '))
  enteros.append(numero)

for x in enteros:
  if x % 2 == 0:
    numeros_pares.append(x)
    
par_maximo = max(numeros_pares)
posicion = enteros.index(par_maximo)

print(f'El número mayor par "{par_maximo}", se encuentra en la posición "{posicion}".')