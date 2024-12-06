# Leer un número entero y determinar si es un número capicúa. Ej. 15651, 59895.
entero = int(input('Entero: '))
entero = str(entero)

entero_invertido = entero[::-1] 

if entero == entero_invertido:
  print(f'El número {entero} es un número capicúa')

else:
  print(f'El número {entero} no es un número capicúa')