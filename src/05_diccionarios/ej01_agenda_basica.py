#!/usr/bin/env python3
"""
Ejercicio:
Agenda básica.
- Pide N contactos (nombre -> teléfono) y los guarda en un diccionario.
- Luego pide un nombre y muestra su teléfono si existe.
"""

agenda = {}

n = int(input("¿Cuántos contactos vas a introducir?: "))

for _ in range(n):
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()

    # Si el nombre se repite, se actualiza el teléfono
    agenda[nombre] = telefono

buscar = input("Nombre a buscar: ").strip()

if buscar in agenda:
    print("Teléfono:", agenda[buscar])
else:
    print("No encontrado")
