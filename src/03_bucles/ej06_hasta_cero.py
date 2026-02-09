#!/usr/bin/env python3
"""
Ejercicio:
Pide números hasta introducir 0.
Muestra la suma total y cuántos números se han introducido (sin contar el 0).
"""

suma = 0
contador = 0

x = float(input("Número (0 para terminar): "))

while x != 0:
    suma += x
    contador += 1
    x = float(input("Número (0 para terminar): "))

print("Cantidad:", contador)
print("Suma:", suma)
