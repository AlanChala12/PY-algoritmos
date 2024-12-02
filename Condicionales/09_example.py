# Leer un número entero y determinar si es un número terminado en 4.

try:
  number = int(input('Entero: '))
  ultimo_digito = number % 10
  
  if ultimo_digito == 4:
    print('-El número proporcionado termina en 4-')
  else:
    print('-El número proporcionado no termina en 4-')

except:
  print('---FORMATO INVALIDO---')