# Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos.
try:
  num = int(input('Ingresa un número entero: '))
  is_prim = True
  primos = 0
  
  if 10 <= num < 100:
    dig1 = num // 10
    dig2 = num % 10
    
    for i in range(2, dig1):
      if dig1 % 2 == 0:
        is_prim = False
        break
      
    if is_prim:
      primos += 1
      is_prim = True
        
    for i in range(2, dig2):
      if dig1 % 2 == 0:
        is_prim = False
        break
      
    if is_prim:
      primos += 1
              
    if primos == 2:
      print(f'Ambos dígitos, del número {num} !SON PRIMOS¡')
    elif primos == 1:
      print(f'Solo un dígito, del número {num} !ES PRIMOS¡')
    else:
      print(f'Ningún dígito del número {num}, es primo')
    
  else:
    print('Por favor, ingresa un número entero comprendido entre 10 y 99')
  
except ValueError:
  print('Por favor, ingresa valores númericos')
