#!/usr/bin/env python3
"""
Ejercicio:
Pide un número entero N y muestra los números del 1 al N.
"""

n = int(input("N: "))

if n <= 0:
    print("N debe ser mayor que 0")
else:
    for i in range(1, n + 1):
        print(i)
