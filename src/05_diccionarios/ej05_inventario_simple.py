#!/usr/bin/env python3
"""
Ejercicio:
Inventario simple (producto -> cantidad) con menú:
1) Añadir stock
2) Quitar stock
3) Consultar producto
4) Salir
"""

inventario = {}

while True:
    print("\n1) Añadir stock")
    print("2) Quitar stock")
    print("3) Consultar producto")
    print("4) Salir")
    op = input("Opción: ").strip()

    if op == "1":
        prod = input("Producto: ").strip()
        cant = int(input("Cantidad a añadir: "))
        if cant < 0:
            print("Cantidad inválida")
        else:
            inventario[prod] = inventario.get(prod, 0) + cant
            print("OK. Stock:", inventario[prod])

    elif op == "2":
        prod = input("Producto: ").strip()
        cant = int(input("Cantidad a quitar: "))
        if cant < 0:
            print("Cantidad inválida")
        else:
            actual = inventario.get(prod, 0)
            if cant > actual:
                print("No hay stock suficiente. Stock actual:", actual)
            else:
                inventario[prod] = actual - cant
                print("OK. Stock:", inventario[prod])

    elif op == "3":
        prod = input("Producto: ").strip()
        print("Stock:", inventario.get(prod, 0))

    elif op == "4":
        print("Saliendo...")
        break

    else:
        print("Opción incorrecta")
