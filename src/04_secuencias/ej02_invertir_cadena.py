#!/usr/bin/env python3
"""
Ejercicio:
Pide una cadena y muéstrala invertida (al revés).
"""

texto = input("Texto: ")

invertido = ""
for ch in texto:
    invertido = ch + invertido

print("Invertido:", invertido)
