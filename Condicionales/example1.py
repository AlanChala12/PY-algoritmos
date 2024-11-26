# Calculadora simple
primer_numero = int(input('Primer número: '))

operador = input('''                 
                suma = +
                resta = -
                multiplicación = *
                división = /
                división entera = //
                exponenciación = **
                modul = %
                
                Operador: 
                 ''')

segundo_numero = int(input('Segundo número: '))

print()
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
    
else:
    print('--Formato invalido--')