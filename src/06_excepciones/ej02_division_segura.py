#!/usr/bin/env python3
"""
Ejercicio:
Pedir dos números y hacer la división de forma segura:
- Controlar entradas inválidas (ValueError)
- Controlar división por cero
"""

while True:
    try:
        a = float(input("Numerador: ").strip())
        b = float(input("Denominador: ").strip())
    except ValueError:
        print("Error: introduce números válidos.")
        continue

    if b == 0:
        print("Error: división por cero. Vuelve a intentarlo.")
        continue

    print("Resultado:", a / b)
    break
