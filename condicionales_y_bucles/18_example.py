# Leer un número entero y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.

number = int(input('Entero: '))

if number < 10:
  for x in range(1, number + 1):
    print(x)

elif number >= 10 and number < 100:
  digitos = []

  while number != 0:
    ultimo_digito = number % 10
    digitos.append(ultimo_digito)
    number //= 10

  valor_max = max(digitos)
  valor_min = min(digitos)

  for y in range(valor_min, valor_max + 1):
    print(y)
  
elif number >= 100 and number < 1000:
  digitos2 = []

  while number != 0:
    ultimo_digito2 = number % 10
    digitos2.append(ultimo_digito2)
    number //= 10

  valor_max2 = max(digitos2)
  valor_min2 = min(digitos2)

  for z in range(valor_min2, valor_max2 + 1):
    print(z)

else:
  print('--El número proporcionado, es muy grande--')