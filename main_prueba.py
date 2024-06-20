import funciones as fn

pedidos = []

try:
    while True:
        print(" ")
        print("Menu")
        print("1. Registrar pedido")
        print("2. Listar los todos los pedidos")
        print("3. Imprimir hoja de rutao")
        print("4. Salir del programa")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            fn.registrar_pedido(pedidos)

        elif opcion == 2:
            fn.listar_pedidos(pedidos)

        elif opcion == 3:
            fn.imprimir_hoja(pedidos)

        elif opcion == 4:
            print("Salir del programa")
            break

        else:
            print("Ingrese opcion valida")

except ValueError:
    print("ingrese opcion valida")
