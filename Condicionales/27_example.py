# Leer un número entero y determinar si termina en 7. 

try:
  entero = int(input('Número: '))

  if entero % 10 == 7:
    print('Termina en siete')
  else:
    print('No termina en siete')
    
except ValueError:
  print('Ingresa valores numéricos')