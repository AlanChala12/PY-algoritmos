#Calculadora simple
primer_numero = int(input('Ingresa un número entero: '))
operador = input('¿Cuál será el operador? +, -, *, /, %, //, **:  ')
segundo_numero = int(input('Ingresa otro número entero: '))


if operador == "+":
    print(primer_numero + segundo_numero)

elif operador == "-":
    print(primer_numero - segundo_numero)

elif operador == "*":
    print(primer_numero * segundo_numero)

elif operador == "/":
    print(primer_numero / segundo_numero)

elif operador == "//":
    print(primer_numero // segundo_numero)

elif operador == "%":
    print(primer_numero % segundo_numero)

elif operador == "**":
    print(primer_numero ** segundo_numero)