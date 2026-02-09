#!/usr/bin/env python3
"""
Ejercicio:
Diccionario de traducciones (español -> inglés).
- Pide N parejas de palabras y las guarda.
- Luego pide una palabra en español y muestra su traducción si existe.
"""

trad = {}

n = int(input("¿Cuántas traducciones vas a introducir?: "))

for _ in range(n):
    es = input("Español: ").strip().lower()
    en = input("Inglés: ").strip().lower()
    trad[es] = en

buscar = input("Palabra a traducir (español): ").strip().lower()

if buscar in trad:
    print("Traducción:", trad[buscar])
else:
    print("No está en el diccionario")
