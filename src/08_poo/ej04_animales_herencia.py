#!/usr/bin/env python3
"""
Ejercicio:
Herencia:
- Animal (método sonido)
- Perro y Gato heredan y redefinen sonido
"""

class Animal:
    def sonido(self) -> None:
        print("Sonido genérico")

class Perro(Animal):
    def sonido(self) -> None:
        print("Guau")

class Gato(Animal):
    def sonido(self) -> None:
        print("Miau")


print("1) Perro")
print("2) Gato")
op = input("Elige animal (1/2): ").strip()

if op == "1":
    a = Perro()
    a.sonido()
elif op == "2":
    a = Gato()
    a.sonido()
else:
    print("Opción incorrecta")
