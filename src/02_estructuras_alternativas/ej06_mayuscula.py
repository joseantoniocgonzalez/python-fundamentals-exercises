#!/usr/bin/env python3
"""
Ejercicio:
Lee un carácter y comprueba si es una letra mayúscula.
"""

letra = input("Letra: ")

if len(letra) == 1 and "A" <= letra <= "Z":
    print("Mayuscula")
else:
    print("No mayuscula")
