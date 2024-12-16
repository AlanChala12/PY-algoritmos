# Construir una función que reciba como parámetros dos números enteros y retorne el valor del mayor.
def numero_mayor(n1, n2):
  mayor = max(n1, n2)
  return mayor

entero_uno = int(input('Ingresa un número entero:'))
entero_dos = int(input('Ingresa otro número entero: '))
print(f'El número mayor, es {numero_mayor(entero_uno, entero_dos)}.')