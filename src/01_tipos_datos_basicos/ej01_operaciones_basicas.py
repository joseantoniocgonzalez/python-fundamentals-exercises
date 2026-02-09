#!/usr/bin/env python3
"""
Ejercicio:
Lee dos números y muestra suma, resta, multiplicación y división.
Controla la división por cero.
"""

a = float(input("Número 1: "))
b = float(input("Número 2: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)

if b == 0:
    print("División: error (división por cero)")
else:
    print("División:", a / b)
