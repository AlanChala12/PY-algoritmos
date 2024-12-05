# Leer un número entero y determinar si termina en 7. 
entero = int(input('Entero: '))
ultimo_digito = entero % 10

if ultimo_digito == 7:
  print(f'El número {entero} termina en 7.')
else:
  print(f'El número {entero} no termina en 7.')