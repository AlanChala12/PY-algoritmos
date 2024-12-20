# Cargar un vector de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci y mostrarlo en pantalla.
fibonacci_numeros = []
n1 = 0
n2 = 1

for i in range(0, 10):
  fibonacci_numeros.append(n1)

  fib = n1 + n2
  n1 = n2
  n2 = fib

print(fibonacci_numeros)