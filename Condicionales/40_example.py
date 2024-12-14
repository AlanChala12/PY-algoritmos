# Leer un número entero de 2 dígitos y, si termina en 1, mostrar en pantalla su primer dígito; si termina en 2, mostrar en pantalla la suma de sus dígitos y, si termina en 3, mostrar en pantalla el producto de sus dos dígitos.

entero = int(input('Entero: '))

if 10 <= entero < 100:
  
  primer_digito = entero // 10
  ultimo_digito = entero % 10

  if ultimo_digito == 1:
    print(primer_digito)
  
  elif ultimo_digito == 2:
    print(primer_digito + ultimo_digito)

  elif ultimo_digito == 3:
    print(primer_digito * ultimo_digito)

  else:
    print(f'Número proporcionado {entero}')

else:
  print('Dígita un número que contenga dos dígitos')