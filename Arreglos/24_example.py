# Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición está el menor número primo.

numeros = [int(input(f'Entero {i + 1}: ')) for i in range(10)]
primos = []
es_primo = True

for i in numeros:

  for x in range(2, i):
    if i % x == 0:
      es_primo = False
      break
  else:
    primos.append(i)

min_primo = min(primos)
posicion = primos.index(min_primo) + 1
print(f'El menor número primo "{min_primo}" se encuentra en la posición {posicion} del vector {numeros}')