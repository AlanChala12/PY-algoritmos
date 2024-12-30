# Construir una función que reciba como parámetro un entero y retorne 1 si dicho entero está entre los 30 primeros elementos de la serie de Fibonacci. Deberá retornar 0 si no es así
def fibonacci(entero):

  fib_numeros = []
  n1 = 0
  n2 = 1

  for i in range(0, 30):
    fib_numeros.append(n1)

    fib = n1 + n2
    n1 = n2
    n2 = fib

  if entero in fib_numeros:
    return 1
  else:
    return 0
  
numero = int(input('Ingresa un número entero: '))
print(fibonacci(numero))