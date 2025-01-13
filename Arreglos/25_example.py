# Leer 10 números enteros, almacenarlos en un vector y determinar cuántos de los números leídos son números primos terminados en 3

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

terminados_en_tres = 0

for z in primos:
  if z % 10 == 3:
    terminados_en_tres += 1

print(f'Los cantidad de números primos terminados en tres, del vector {numeros}, son: {terminados_en_tres}')