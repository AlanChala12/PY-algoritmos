# Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne la cantidad de números que pertenecen a los 30 primeros elementos de la serie de Fibonacci.

def fibonacci(vector):
  numeros_fib = []
  esta_en_fib = 0
  n1 = 0
  n2 = 1

  for i in range(1, 31):
    numeros_fib.append(n1)

    fib = n1 + n2
    n1 = n2
    n2 = fib

  for y in vector:
    if y in numeros_fib:
      esta_en_fib += 1

  if esta_en_fib > 0:
    return f'La cantidad de números que pertenecen a los primeros 30 números de la serie de Fibonacci son: {esta_en_fib}.'
  else:
    return f'No se encontraron números que estén en los primeros 30 números de la serie de Fibonacci.'

try:
    numeros = [int(input(f'Entero {i+1}: ')) for i in range(10)]
    print(fibonacci(numeros))
    
except ValueError:
    print('Por favor, ingresa valores numéricos válidos')