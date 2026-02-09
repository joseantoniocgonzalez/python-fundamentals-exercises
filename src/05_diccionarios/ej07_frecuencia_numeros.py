#!/usr/bin/env python3
"""
Ejercicio:
Pide N números enteros y cuenta cuántas veces aparece cada uno.
"""

n = int(input("N: "))

if n <= 0:
    print({})
else:
    freq = {}

    for _ in range(n):
        x = int(input("Número: "))
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    print(freq)
