# Construir una función que reciba como parámetro un vector de 10 posiciones enteras y retorne la cantidad de números primos almacenados en el vector.

numeros = []

for i in range(1, 11):
  numero = int(input(f'Entero {i}: '))
  numeros.append(numero)

def es_primo(vector):

  def es_numero_primo(n):
    if n <= 1:
      return False
      
    for i in range(2, n):
      if n % i == 0:
        return False
    return True

  cantidad_primos = sum(1 for z in vector if es_numero_primo(z))
  return cantidad_primos

print(f'Cantidad de números primos: {es_primo(numeros)}')