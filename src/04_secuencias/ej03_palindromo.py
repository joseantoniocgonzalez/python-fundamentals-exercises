#!/usr/bin/env python3
"""
Ejercicio:
Pide un texto e indica si es palíndromo.
Ignora espacios y mayúsculas/minúsculas.
"""

texto = input("Texto: ")

normalizado = ""
for ch in texto.lower():
    if ch != " ":
        normalizado += ch

invertido = normalizado[::-1]

if normalizado == invertido and normalizado != "":
    print("Es palíndromo")
else:
    print("No es palíndromo")
