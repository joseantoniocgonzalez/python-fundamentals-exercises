#!/usr/bin/env python3
"""
Ejercicio:
Pide una cadena y cuenta cuántas vocales contiene.
"""

texto = input("Texto: ")

vocales = "aeiouáéíóúü"
contador = 0

for ch in texto.lower():
    if ch in vocales:
        contador += 1

print("Vocales:", contador)
