#!/usr/bin/env python3
"""
Ejercicio:
Pide un texto y cuenta cuántas veces aparece cada palabra.
"""

texto = input("Texto: ").lower().strip()

if texto == "":
    print({})
else:
    palabras = texto.split()
    freq = {}

    for p in palabras:
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    print(freq)
