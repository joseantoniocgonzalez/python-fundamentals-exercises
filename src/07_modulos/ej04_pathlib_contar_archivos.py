#!/usr/bin/env python3
"""
Ejercicio:
Usar pathlib:
- Pedir una ruta de carpeta
- Contar cuántos archivos y cuántas subcarpetas hay (no recursivo)
"""

from pathlib import Path

ruta = input("Ruta de carpeta (vacío = carpeta actual): ").strip()
if ruta == "":
    ruta = "."

p = Path(ruta)

if not p.exists():
    print("Error: la ruta no existe.")
elif not p.is_dir():
    print("Error: la ruta no es una carpeta.")
else:
    archivos = 0
    carpetas = 0

    for item in p.iterdir():
        if item.is_file():
            archivos += 1
        elif item.is_dir():
            carpetas += 1

    print("Carpeta:", p.resolve())
    print("Archivos:", archivos)
    print("Subcarpetas:", carpetas)
