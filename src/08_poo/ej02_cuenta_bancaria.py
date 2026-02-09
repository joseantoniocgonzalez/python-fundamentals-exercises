#!/usr/bin/env python3
"""
Ejercicio:
Clase CuentaBancaria:
- atributo: saldo
- métodos: ingresar, retirar, mostrar_saldo
- menú para operar
"""

class CuentaBancaria:
    def __init__(self, saldo: float = 0.0):
        self.saldo = saldo

    def ingresar(self, cantidad: float) -> None:
        if cantidad < 0:
            print("Cantidad inválida.")
            return
        self.saldo += cantidad
        print("Ingreso OK. Saldo:", self.saldo)

    def retirar(self, cantidad: float) -> None:
        if cantidad < 0:
            print("Cantidad inválida.")
            return
        if cantidad > self.saldo:
            print("No hay saldo suficiente. Saldo:", self.saldo)
            return
        self.saldo -= cantidad
        print("Retirada OK. Saldo:", self.saldo)

    def mostrar_saldo(self) -> None:
        print("Saldo:", self.saldo)


cuenta = CuentaBancaria()

while True:
    print("\n1) Ingresar")
    print("2) Retirar")
    print("3) Ver saldo")
    print("4) Salir")
    op = input("Opción: ").strip()

    if op == "4":
        print("Saliendo...")
        break
    elif op == "1":
        try:
            c = float(input("Cantidad a ingresar: ").strip())
        except ValueError:
            print("Error: número inválido.")
            continue
        cuenta.ingresar(c)
    elif op == "2":
        try:
            c = float(input("Cantidad a retirar: ").strip())
        except ValueError:
            print("Error: número inválido.")
            continue
        cuenta.retirar(c)
    elif op == "3":
        cuenta.mostrar_saldo()
    else:
        print("Opción incorrecta.")
