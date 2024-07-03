from funciones import *
while True:
    limpiar_pantalla()
    print("Gaxplosive")
    print("1. Registrar pedido.")
    print("2. Listar todos los pedidos.")
    print("3. Buscar pedido por RUT.")
    print("4. Imprimir hoja de ruta.")
    print("5. Salir del programa.")
    opcion=int(input("igrese la opcion que desee: "))
    if opcion==1:
        opcion1()
    elif opcion==2:
        opcion2()
    elif opcion==3:
        opcion3()
    elif opcion==4:
        opcion4()
    else:
        opcion5()
        break
