# Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición está el número con más dígitos.
enteros = []

for i in range(1, 11):
  numeros = int(input(f'Entero {i}: '))
  enteros.append(numeros)

numero_mayor = max(enteros)

if numero_mayor in enteros:
    print(f'El número con más dígitos "{numero_mayor}" se encuentra en el índice {enteros.index(numero_mayor)}')

print(enteros)