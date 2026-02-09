#!/usr/bin/env python3
"""
Ejercicio:
Pide un número entero N y calcula la suma de 1 a N.
"""

n = int(input("N: "))

if n <= 0:
    print("N debe ser mayor que 0")
else:
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print("Suma:", suma)
