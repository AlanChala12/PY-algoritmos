# Leer un número entero de cuatro dígitos y determinar cuántos dígitos pares tiene.
entero = int(input('Entero: '))
counting = 0

while entero != 0:
  ultimo_digito = entero % 10

  if ultimo_digito % 2 == 0:
    counting += 1
  
  entero //= 10

print(f'La cantidad de dígitos pares del número proporcionado es de {counting}')