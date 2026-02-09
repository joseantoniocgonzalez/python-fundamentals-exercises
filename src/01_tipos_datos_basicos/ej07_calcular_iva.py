#!/usr/bin/env python3
"""
Ejercicio:
Pide un precio base y un porcentaje de IVA.
Muestra el importe del IVA y el precio final.
"""

base = float(input("Precio base: "))
iva_pct = float(input("IVA (%): "))

if base < 0 or iva_pct < 0:
    print("Precio e IVA deben ser 0 o mayores")
else:
    iva = base * (iva_pct / 100)
    total = base + iva

    print("IVA:", iva)
    print("Total:", total)
