# Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

entero = int(input('Entero: '))

if entero < 10 or entero >= 100:
  print('Ingresa un número que contenga dos diígitos')
  
else:
  dig1 = entero // 10
  dig2 = entero % 10
  
  if dig1 % 2 == 0 and dig2 % 2 == 0:
    print(f'Los dígitos que comforman al número {entero} son pares')
    
  elif dig1 % 2 == 0 or dig2 % 2 == 0:
    print(f'Solo un dígito del número {entero} es par')
    
  else:
    print(f'Los dígitos que conforman al número {entero} no son pares')