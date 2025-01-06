# Construir una función que reciba como parámetros un vector de 10 posiciones enteras y un valor entero y retorne 1 si dicho valor entero se encuentra en el vector. Deberá retornar 0 si no es así.

def isInVector(vector, numero):
  if numero in vector:
    return 1
  else:
    return 0

try:
    numeros = [int(input(f'Entero {i + 1}: ')) for i in range(10)]
    entero = int(input('Ingresa un número entero: '))
    print(isInVector(numeros, entero))
    
except ValueError:
    print('Por favor, ingresa valores numéricos válidos')