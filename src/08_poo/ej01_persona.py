#!/usr/bin/env python3
"""
Ejercicio:
Clase Persona:
- atributos: nombre, edad
- método: saludar()
"""

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self) -> None:
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


nombre = input("Nombre: ").strip()

try:
    edad = int(input("Edad: ").strip())
except ValueError:
    print("Error: la edad debe ser un entero.")
    raise SystemExit(1)

p = Persona(nombre, edad)
p.saludar()
