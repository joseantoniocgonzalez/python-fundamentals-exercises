#!/usr/bin/env python3
"""
Ejercicio:
Pide N alumnos (nombre -> nota).
Muestra la media y el alumno con mejor nota.
"""

notas = {}

n = int(input("¿Cuántos alumnos?: "))

if n <= 0:
    print("N debe ser mayor que 0")
else:
    for _ in range(n):
        nombre = input("Nombre: ").strip()
        nota = float(input("Nota: "))
        notas[nombre] = nota  # si se repite, se actualiza

    total = 0.0
    mejor_nombre = None
    mejor_nota = None

    for nombre, nota in notas.items():
        total += nota
        if mejor_nota is None or nota > mejor_nota:
            mejor_nota = nota
            mejor_nombre = nombre

    media = total / len(notas)

    print("Media:", media)
    print("Mejor alumno:", mejor_nombre)
    print("Mejor nota:", mejor_nota)
