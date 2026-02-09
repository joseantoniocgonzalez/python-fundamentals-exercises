#!/usr/bin/env python3
"""
Ejercicio:
Adivina el número.
El programa genera un número entre 1 y 100 y el usuario intenta acertarlo.
"""

import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    x = int(input("Adivina (1-100): "))
    intentos += 1

    if x < secreto:
        print("Más alto")
    elif x > secreto:
        print("Más bajo")
    else:
        print("¡Correcto!")
        print("Intentos:", intentos)
        break
