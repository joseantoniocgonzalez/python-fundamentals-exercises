#!/usr/bin/env python3
"""
Ejercicio:
Pide dos valores y muestra el intercambio de variables (a <-> b).
"""

a = input("Valor A: ")
b = input("Valor B: ")

print("Antes -> A:", a, "| B:", b)

a, b = b, a

print("Después -> A:", a, "| B:", b)
