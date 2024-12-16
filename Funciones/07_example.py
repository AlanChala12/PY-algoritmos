# Construir una función que reciba como parámetro un entero y un dígito y retorne la cantidad de veces que se encuentra dicho dígito en dicho entero.
def numero_de_veces(n, d):
  entero = str(n)
  dig = str(d)
  apariciones = 0
  
  for x in entero:
    if dig == x:
      apariciones += 1 
    
  return apariciones

entero = int(input('Ingresa un número entero: '))
digito = int(input('Ingresa un dígito: '))
result = numero_de_veces(entero, digito)
print(f'El dígito {digito} está presente en el número {entero}, {result} vez/veces')