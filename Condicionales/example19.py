# Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.

number = int(input('Ingresa un número entero positivo de tres dígitos: '))

if number >= 100 and number < 100:
    xx = number // 10
    dig1 = xx // 10
    dig2 = xx % 10
    dig3 = number % 10

    if dig2 % dig1 == 0:
        print(f'{dig1} es múltiplo de {dig2}.')

    elif dig3 % dig1 == 0:
      print(f'{dig1} es múltiplo de {dig3}.')

    elif dig1 % dig2 == 0:
      print(f'{dig2} es múltiplo de {dig1}.')

    elif dig1 % dig3 == 0:
      print(f'{dig3} es múltiplo de {dig1}.')

    elif dig2 % dig3 == 0:
      print(f'{dig3} es múltiplo de {dig2}.')

    elif dig3 % dig2 == 0:
      print(f'{dig2} es múltiplo de {dig3}.')
  
    else:
      print(f'Ningún dígito que conforma el número {number}, es múltiplo de otro dígito del mismo número.')

