#!/usr/bin/env python3
"""
Ejercicio:
Pedir un número decimal (float).
Si el usuario mete algo inválido, volver a pedirlo hasta que sea correcto.
"""

while True:
    texto = input("Introduce un número (puede ser decimal): ").strip()
    try:
        x = float(texto)
        print("Correcto. Has introducido:", x)
        break
    except ValueError:
        print("Error: eso no es un número válido. Inténtalo otra vez.")
