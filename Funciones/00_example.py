# Construir una función que reciba como parámetro un entero y retorne su último dígito.
def ultimo_digito(entero):
    x = entero % 10
    return x

number = int(input('Ingresa un número entero: '))
ultimo = ultimo_digito(number)

print(f'El último dígito del número {number} es "{ultimo}"')