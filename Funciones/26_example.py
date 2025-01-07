# Construir una función que reciba como parámetros dos enteros, el primero actuará como base y el segundo como exponente, y retorne el resultado de elevar dicha base a dicho exponente.
exponenciacion = lambda base, expo : base ** expo

try:
  base = int(input('Base: '))
  exponente = int(input('Exponente: '))

  print(exponenciacion(base, exponente))
except ValueError:
  print('**Por favor, ingresa valores numéricos**')