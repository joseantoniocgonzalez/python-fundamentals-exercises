#!/usr/bin/env python3
"""
Ejercicio:
Usar el módulo random:
- Simular tiradas de un dado (1..6)
- Pedir cuántas tiradas hacer
- Contar cuántas veces sale cada cara
"""

import random

try:
    n = int(input("¿Cuántas tiradas?: ").strip())
except ValueError:
    print("Error: debes introducir un entero.")
    raise SystemExit(1)

if n <= 0:
    print("N debe ser mayor que 0")
else:
    conteo = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(n):
        cara = random.randint(1, 6)
        conteo[cara] += 1

    print("Resultados:")
    for cara in range(1, 7):
        print(cara, "->", conteo[cara])
