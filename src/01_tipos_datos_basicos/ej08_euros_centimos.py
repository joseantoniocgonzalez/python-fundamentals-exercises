#!/usr/bin/env python3
"""
Ejercicio:
Conversor Euros <-> Céntimos.

Opciones:
1) Euros -> Céntimos
2) Céntimos -> Euros
"""

print("1) Euros -> Céntimos")
print("2) Céntimos -> Euros")

op = input("Elige opción (1/2): ").strip()

if op == "1":
    euros = float(input("Euros: "))
    if euros < 0:
        print("Los euros deben ser 0 o mayores")
    else:
        cent = round(euros * 100)
        print("Céntimos:", cent)
elif op == "2":
    cent = int(input("Céntimos: "))
    if cent < 0:
        print("Los céntimos deben ser 0 o mayores")
    else:
        euros = cent / 100
        print("Euros:", euros)
else:
    print("Opción incorrecta")
