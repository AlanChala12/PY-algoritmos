# Calculadora simple.

def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b): return a / b if b != 0 else "Error: División entre cero"
def modulo(a, b): return a % b if b != 0 else "Error: División entre cero"
def exponenciacion(a, b): return a ** b
def division_entera(a, b): return a // b if b != 0 else "Error: División entre cero"

operaciones = {
    '1': suma,
    '2': resta,
    '3': multiplicacion,
    '4': division,
    '5': modulo,
    '6': exponenciacion,
    '7': division_entera
}

menu = """
¡BIENVENIDO! Operaciones disponibles:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Módulo
6. Exponenciación
7. División entera
8. Salir
"""

while True:
    print(menu)
    decision_del_usuario = input('Selecciona una operación (1-8): ')

    if decision_del_usuario == '8':
        print("Cerrando...")
        break

    if decision_del_usuario not in operaciones:
        print("¡Formato inválido! Por favor, elige una opción válida [1-8].")
        continue

    try:
        valor1 = int(input('Valor 1: '))
        valor2 = int(input('Valor 2: '))
        
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")
        continue

    resultado = operaciones[decision_del_usuario](valor1, valor2)
    print(f"El resultado es: {resultado}")