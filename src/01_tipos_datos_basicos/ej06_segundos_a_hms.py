#!/usr/bin/env python3
"""
Ejercicio:
Pide un número entero de segundos y lo convierte a formato hh:mm:ss.
"""

total = int(input("Segundos: "))

if total < 0:
    print("Los segundos deben ser 0 o mayores")
else:
    horas = total // 3600
    resto = total % 3600
    minutos = resto // 60
    segundos = resto % 60

    # Formato con 2 dígitos para minutos y segundos (y horas también)
    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
