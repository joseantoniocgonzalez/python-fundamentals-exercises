#!/usr/bin/env python3
"""
Ejercicio:
Pide dos números y una operación (+, -, *, /) y muestra el resultado.
Controla división por cero y operación inválida.
"""

a = float(input("Número 1: "))
b = float(input("Número 2: "))
op = input("Operación (+, -, *, /): ").strip()

if op == "+":
    print("Resultado:", a + b)
elif op == "-":
    print("Resultado:", a - b)
elif op == "*":
    print("Resultado:", a * b)
elif op == "/":
    if b == 0:
        print("Error: división por cero")
    else:
        print("Resultado:", a / b)
else:
    print("Operación incorrecta")
