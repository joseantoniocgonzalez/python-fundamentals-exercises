#!/usr/bin/env python3
"""
Ejercicio:
Conversor Celsius <-> Fahrenheit.

Opciones:
1) Celsius -> Fahrenheit
2) Fahrenheit -> Celsius
"""

print("1) Celsius -> Fahrenheit")
print("2) Fahrenheit -> Celsius")

op = input("Elige opción (1/2): ").strip()

if op == "1":
    c = float(input("Celsius: "))
    f = (c * 9 / 5) + 32
    print("Fahrenheit:", f)
elif op == "2":
    f = float(input("Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("Celsius:", c)
else:
    print("Opción incorrecta")
