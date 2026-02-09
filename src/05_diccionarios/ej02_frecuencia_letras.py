#!/usr/bin/env python3
"""
Ejercicio:
Pide un texto y cuenta la frecuencia de cada letra (ignorando espacios).
"""

texto = input("Texto: ").lower()

freq = {}

for ch in texto:
    if ch == " ":
        continue

    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
