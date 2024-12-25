# Leer 10 números enteros, almacenarlos en un vector y determinar cuál es el número menor.
enteros = []
negativos = 0

for i in range(1, 11):
  numeros = int(input(f'Entero {i}: '))
  enteros.append(numeros)

print(f'El valor mínimo del vector {enteros} es {min(enteros)}')