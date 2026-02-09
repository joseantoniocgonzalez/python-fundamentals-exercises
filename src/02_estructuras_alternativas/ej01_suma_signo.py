#!/usr/bin/env python3
"""
Ejercicio:
Lee dos números y muestra si su suma es positiva, negativa o cero.
"""

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

suma = num1 + num2

if suma > 0:
    print("Suma positiva")
elif suma < 0:
    print("Suma negativa")
else:
    print("Suma es 0")
