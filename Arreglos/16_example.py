# Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números negativos hay.
enteros = []
negativos = 0

for i in range(1, 11):
  numeros = int(input(f'Entero {i}: '))
  enteros.append(numeros)

for x in enteros:
  if x < 0:
    negativos += 1

if negativos == 0:
  print(f'No hay número negativos en el vector {enteros}')
else:
  print(f'Hay {negativos} números negativos en el vector')