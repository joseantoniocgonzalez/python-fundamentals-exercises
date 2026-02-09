#!/usr/bin/env python3
"""
Ejercicio:
Menú simple con validación:
1) Sumar dos enteros
2) Restar dos enteros
3) Salir

Controlar:
- Opción inválida
- Entradas no numéricas
"""

while True:
    print("\n--- MENÚ ---")
    print("1) Sumar")
    print("2) Restar")
    print("3) Salir")

    op = input("Opción: ").strip()

    if op == "3":
        print("Saliendo...")
        break

    if op not in ("1", "2"):
        print("Opción incorrecta.")
        continue

    try:
        a = int(input("Entero 1: ").strip())
        b = int(input("Entero 2: ").strip())
    except ValueError:
        print("Error: debes introducir enteros.")
        continue

    if op == "1":
        print("Resultado:", a + b)
    else:
        print("Resultado:", a - b)
