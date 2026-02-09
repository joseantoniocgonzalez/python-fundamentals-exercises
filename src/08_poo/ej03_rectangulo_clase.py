#!/usr/bin/env python3
"""
Ejercicio:
Clase Rectangulo:
- atributos: base, altura
- métodos: area(), perimetro()
"""

class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)


try:
    base = float(input("Base: ").strip())
    altura = float(input("Altura: ").strip())
except ValueError:
    print("Error: debes introducir números.")
    raise SystemExit(1)

if base <= 0 or altura <= 0:
    print("Error: base y altura deben ser mayores que 0.")
else:
    r = Rectangulo(base, altura)
    print("Área:", r.area())
    print("Perímetro:", r.perimetro())
