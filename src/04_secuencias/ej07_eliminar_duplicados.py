#!/usr/bin/env python3
"""
Ejercicio:
Pide N números, guarda en una lista y crea otra lista sin duplicados
manteniendo el orden (sin usar set).
"""

n = int(input("N: "))

if n <= 0:
    print("N debe ser mayor que 0")
else:
    numeros = []
    for _ in range(n):
        x = float(input("Número: "))
        numeros.append(x)

    sin_duplicados = []
    for x in numeros:
        if x not in sin_duplicados:
            sin_duplicados.append(x)

    print("Original:", numeros)
    print("Sin duplicados:", sin_duplicados)
