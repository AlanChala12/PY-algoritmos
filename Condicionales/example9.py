# Leer un número entero y determinar si es un número terminado en 4.
try:
  user_number = int(input('Ingresa un número entero positivo: '))

  ultimo_digito = (user_number // 10) * 10
  ultimo_digito = user_number - ultimo_digito

  if ultimo_digito == 4:
    print('---El número proporcionado termina en 4---')

  else:
    print('---El número proporcionado no termina en 4---')

except:
  print('---FORMATO INVALIDO---')