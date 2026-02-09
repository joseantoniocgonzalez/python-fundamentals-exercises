#!/usr/bin/env python3
"""
Ejercicio:
Pide tres números e indica cuál es el mayor.
"""

a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c

print("El mayor es:", mayor)
