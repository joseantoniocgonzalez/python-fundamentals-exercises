#!/usr/bin/env python3
"""
Ejercicio:
Pide N números, guarda en una lista y luego pide un número a buscar.
Indica si está y su primera posición (índice).
"""

n = int(input("N: "))

if n <= 0:
    print("N debe ser mayor que 0")
else:
    numeros = []
    for _ in range(n):
        x = float(input("Número: "))
        numeros.append(x)

    objetivo = float(input("Número a buscar: "))

    encontrado = False
    posicion = -1

    for i in range(len(numeros)):
        if numeros[i] == objetivo:
            encontrado = True
            posicion = i
            break

    if encontrado:
        print("Encontrado en posición:", posicion)
    else:
        print("No encontrado")
