#!/usr/bin/env python3
"""
Ejercicio:
Pide nombre, edad y ciudad.
Guarda los datos en una tupla y muéstralos formateados.
"""

nombre = input("Nombre: ")
edad = int(input("Edad: "))
ciudad = input("Ciudad: ")

persona = (nombre, edad, ciudad)

print("Nombre:", persona[0])
print("Edad:", persona[1])
print("Ciudad:", persona[2])
