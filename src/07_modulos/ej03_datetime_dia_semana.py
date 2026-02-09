#!/usr/bin/env python3
"""
Ejercicio:
Usar datetime:
- Pedir una fecha en formato YYYY-MM-DD
- Decir qué día de la semana fue/es
"""

import datetime

texto = input("Fecha (YYYY-MM-DD): ").strip()

try:
    fecha = datetime.date.fromisoformat(texto)
except ValueError:
    print("Error: formato inválido. Ejemplo correcto: 2026-02-09")
    raise SystemExit(1)

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
print("Día de la semana:", dias[fecha.weekday()])
