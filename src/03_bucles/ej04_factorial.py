#!/usr/bin/env python3
"""
Ejercicio:
Pide un número entero N y calcula su factorial (N!).
"""

n = int(input("N: "))

if n < 0:
    print("N debe ser mayor o igual que 0")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial:", fact)
