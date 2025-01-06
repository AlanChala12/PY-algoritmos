# Construir una función que reciba como parámetro un entero y retorne ese elemento de la serie de Fibonacci.

def entero_en_fib(entero):
  fib_numeros = []
  n1, n2 = 0, 1

  for i in range(100):
    fib_numeros.append(n1)

    fib = n1 + n2
    n1 = n2
    n2 = fib

  return f'El número que se encuentra en dicho índice de la serie de Fibonacci es {fib_numeros[entero]}.'

try:
  numero = int(input('Ingresa un número entero: '))
  print(entero_en_fib(numero))

except ValueError:
  print('Por favor, ingresa un número entero.')