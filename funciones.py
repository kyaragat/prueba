SECTOR = ["centro", "norte", "sur"]

def registrar_pedido(pedidos):
    print("registrar pedido")
    nombre_cliente= input("Ingrese su nombre y apellido: ").lower()
    direccion_cliente=input("Ingrese su direccion: ").lower()
    sector_cliente=input("ingrese sector centro, norte, o sur: ").lower()
    print("")
    try:
        paquete_pequeno=int(input("ingrese la cantidad de paquetes pequeños: "))
        paquete_mediano=int(input("ingrese la cantidad de paquetes medianos: "))
        paquete_grande=int(input("ingrese la cantidad de paquetes grandes: "))

    except ValueError:
        print("ingrese una cantidad valida o 0")
    
    if nombre_cliente and direccion_cliente and sector_cliente:
        print("Datos guardados")
        print("")
    else:
        print ("debe ingresar todos los datos")
        return

    pedidos.append({
        "Nombre" : nombre_cliente,
        "Direccion" : direccion_cliente,
        "Sector" : sector_cliente,
        "PaqPequenos": paquete_pequeno,
        "PaqMedianos": paquete_mediano,
        "PaqGrandes" : paquete_grande,

    })

def listar_pedidos(pedidos):
    print("Listar pedidos")
    for pedido in pedidos:
        print(pedido)


def imprimir_hoja(pedidos):
    print("Imprimir hoja de ruta")
    sectorSeleccionado = input("ingrese sector centro, norte, sur o presione ENTER para imprimir todos los pedidos: ").lower()
        
    if sectorSeleccionado == "":
        hoja_a_imprimir=pedidos
    elif sectorSeleccionado in SECTOR:
        sector_a_imprimir= []
        for i in pedidos:
            if sectorSeleccionado["sector"] == sectorSeleccionado:
                sector_a_imprimir.append(i)
                hoja_a_imprimir=sector_a_imprimir
    else:
        print("ingrese datos validos")
        return

    import json
    with open ("Impresion_pedidos.json", "w") as archivo:
        json.dump (hoja_a_imprimir, archivo)
        print("datos impresos en formato json")
        
