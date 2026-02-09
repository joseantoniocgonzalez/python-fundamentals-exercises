#!/usr/bin/env python3
"""
Ejercicio:
Pide un número N, lee N números en una lista y muestra:
máximo, mínimo y media.
"""

n = int(input("N: "))

if n <= 0:
    print("N debe ser mayor que 0")
else:
    numeros = []
    for _ in range(n):
        x = float(input("Número: "))
        numeros.append(x)

    maximo = max(numeros)
    minimo = min(numeros)
    media = sum(numeros) / len(numeros)

    print("Lista:", numeros)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)
    print("Media:", media)
