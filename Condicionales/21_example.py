# Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.

x = int(input('Ingresa un entero mayor o igual a cien: '))
x = str(x)
    
if len(x) == 3:
    if "1" in x:
        print('El número proporcionado tiene el dígito uno.')
    else:
        print('El número proporcionado no tiene el dígito uno.')
else:
    print('El número ingresado no tiene tres dígitos.')
