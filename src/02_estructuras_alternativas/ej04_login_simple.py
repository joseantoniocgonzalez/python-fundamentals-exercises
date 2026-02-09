#!/usr/bin/env python3
"""
Ejercicio:
Pide usuario y contraseña.
Si se introduce "pepe" y "asdasd" -> "Has entrado al sistema".
Si no -> "Error".
"""

usuario = input("Usuario: ")
clave = input("Contraseña: ")

if usuario == "pepe" and clave == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error")
