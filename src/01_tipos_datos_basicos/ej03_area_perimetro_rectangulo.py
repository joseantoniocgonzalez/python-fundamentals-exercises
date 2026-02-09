#!/usr/bin/env python3
"""
Ejercicio:
Pide base y altura de un rectángulo y calcula área y perímetro.
"""

base = float(input("Base: "))
altura = float(input("Altura: "))

if base <= 0 or altura <= 0:
    print("Base y altura deben ser mayores que 0")
else:
    area = base * altura
    perimetro = 2 * (base + altura)

    print("Área:", area)
    print("Perímetro:", perimetro)
