#!/usr/bin/env python3
"""
Ejercicio:
Pide un número N y luego lee N números.
Cuenta cuántos son positivos, negativos y ceros.
"""

n = int(input("¿Cuántos números vas a introducir?: "))

positivos = 0
negativos = 0
ceros = 0

for _ in range(n):
    x = float(input("Número: "))
    if x > 0:
        positivos += 1
    elif x < 0:
        negativos += 1
    else:
        ceros += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)
