# Hallar el factorial de un número.

"""Con bucle while"""
user_name = int(input('Ingresa un número entero: '))

counting = user_name
factorial = user_name

while counting > 1:

  counting -= 1
  factorial = factorial * counting

print(factorial)



"""Con bucle for"""
user_number = int(input('Ingresa un valor númerico entero positivo: '))
facto = user_number

for xx in range(1, user_number):

  facto = facto * xx

print(f'{user_number}! = {facto}')