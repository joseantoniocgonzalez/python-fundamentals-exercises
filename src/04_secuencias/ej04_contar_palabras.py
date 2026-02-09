#!/usr/bin/env python3
"""
Ejercicio:
Pide un texto y cuenta cuántas palabras contiene.
"""

texto = input("Texto: ").strip()

if texto == "":
    print("Palabras: 0")
else:
    palabras = texto.split()
    print("Palabras:", len(palabras))
