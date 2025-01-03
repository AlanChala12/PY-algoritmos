import random

def contraseña_aleatorio(longitud = 8):
    
  caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&/()=¡?¿*+-'
  password = ''.join(random.sample(caracteres, longitud))

  return f'Aquí tienes tu contraseña: {password}'

  
def main():
    
  print('--Generador de contraseña--')

  try:
    lon = int(input('Por favor, dígita la longitud de tu contraseña (mínimo 5): '))

    if lon < 5:
      print('Error: La longitud debe ser al menos 5 caracteres.')
    else:
      print(contraseña_aleatorio(longitud = lon))

  except ValueError:
        print('Error: Por favor, ingresa un valor numérico válido.')

if __name__ == "__main__":
    main()