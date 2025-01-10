# Construir una función que reciba como parámetro un vector de 10 posiciones enteras y un dígito y que retorne la cantidad de números del vector que terminan en dicho dígito.

def termina_en(vec, dig):
  contador = 0

  for i in vec:
    if i % 10 == dig:
      contador += 1

  return f'La cantidad de números que terminan en {dig} en el vector {vec}, son: {contador}' 

try:
    numeros = [int(input(f'Entero {i + 1}: ')) for i in range(10)]
    digito = int(input('Ingresa un dígito [0-9]: '))

    if digito < 0 or digito > 9:
        print('Por favor ingresa un dígito entre 0 y 9')
    else:
        print(termina_en(numeros, digito))
  
except ValueError:
    print('**Por favor, ingresa valores numéricos**')