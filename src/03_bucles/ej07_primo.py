#!/usr/bin/env python3
"""
Ejercicio:
Pide un número entero n e indica si es primo o no primo.
"""

n = int(input("n: "))

if n <= 1:
    print("No primo")
else:
    es_primo = True
    limite = int(n ** 0.5)

    for i in range(2, limite + 1):
        if n % i == 0:
            es_primo = False
            break

    if es_primo:
        print("Primo")
    else:
        print("No primo")
