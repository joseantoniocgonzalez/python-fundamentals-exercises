#!/usr/bin/env python3
"""
Ejercicio:
Pedir un número entero por teclado.
Si el usuario mete algo inválido, volver a pedirlo hasta que sea correcto.
"""

while True:
    texto = input("Introduce un entero: ").strip()
    try:
        n = int(texto)
        print("Correcto. Has introducido:", n)
        break
    except ValueError:
        print("Error: eso no es un entero. Inténtalo otra vez.")
