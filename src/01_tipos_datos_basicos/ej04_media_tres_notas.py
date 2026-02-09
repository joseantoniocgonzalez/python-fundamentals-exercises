#!/usr/bin/env python3
"""
Ejercicio:
Pide 3 notas, calcula la media e indica si está aprobado (>= 5) o suspenso.
"""

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1 + n2 + n3) / 3

print("Media:", media)

if media >= 5:
    print("Aprobado")
else:
    print("Suspenso")
