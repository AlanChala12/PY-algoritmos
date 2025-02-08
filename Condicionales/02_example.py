# Leer un número entero de dos dígitos menor que 20 y determinar si es primo.

try:
  num = int(input('Ingresa un número entero: '))
  is_prim = True

  if 10 <= num <= 20:
      for i in range(2, num):
        if num % 2 == 0:
          is_prim = False
          break

      if is_prim:
        print('Es primo')
      else:
        print('No es primo')
        
  else:
    print('Por favor, ingresa un número entero, comprendido entre 10 y 20')
      
  
except ValueError:
  print('Por favor, ingresa un número entero, comprendido entre 10 y 20')