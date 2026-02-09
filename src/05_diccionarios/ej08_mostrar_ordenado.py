#!/usr/bin/env python3
"""
Ejercicio:
Pide N pares (clave -> valor) y muestra el diccionario ordenado por clave.
"""

d = {}

n = int(input("¿Cuántos pares vas a introducir?: "))

for _ in range(n):
    clave = input("Clave: ").strip()
    valor = input("Valor: ").strip()
    d[clave] = valor

print("\n--- Ordenado por clave ---")
for clave in sorted(d.keys()):
    print(clave, "->", d[clave])
