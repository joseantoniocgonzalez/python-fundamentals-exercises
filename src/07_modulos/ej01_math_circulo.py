#!/usr/bin/env python3
"""
Ejercicio:
Usar el módulo math:
- Pedir radio de un círculo
- Calcular área y perímetro
- Mostrar resultados (con redondeo)
"""

import math

try:
    r = float(input("Radio: ").strip())
except ValueError:
    print("Error: radio inválido.")
    raise SystemExit(1)

if r < 0:
    print("Error: el radio debe ser 0 o mayor.")
else:
    area = math.pi * (r ** 2)
    perimetro = 2 * math.pi * r
    print("Área:", round(area, 2))
    print("Perímetro:", round(perimetro, 2))
