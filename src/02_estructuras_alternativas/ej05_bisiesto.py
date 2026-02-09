#!/usr/bin/env python3
"""
Ejercicio:
Lee un año e indica si es bisiesto.
Regla:
- divisible por 4 y no por 100, excepto si también es divisible por 400.
"""

year = int(input("Año: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Bisiesto")
else:
    print("No bisiesto")
