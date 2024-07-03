import csv
import os
import msvcrt

pedidos=[]


def limpiar_pantalla():
    os.system("cls")
def esperar_tecla():
    print("presione cualquier tecla para continuar")
    msvcrt.getch()

def opcion1():
    rut=validar_rut()
    nombre=validar_nombre()
    direccion=validar_direccion()
    comuna=validar_comuna()
    cinco_kg=validar_cilindro5kg
    quince_kg=validar_cilindro15kg

    monto=cinco_kg*12500+quince_kg*25500

    pedido={"rut":rut,
            "cliente":nombre,
            "direccion":direccion,
            "comuna":comuna,
            "cil.5kg":cinco_kg,
            "cil.15kg":quince_kg,
            "Total":monto}
    pedidos.append(pedido)
    limpiar_pantalla()
    print("Pedido agregado")
    esperar_tecla()


def opcion2():
    limpiar_pantalla()
    if len(pedidos)==0:
        print("No hay pedidos por el momento")
    else:
        i=0
        print("Rut        cliente       direccion     comuna     cil.5kg  cil.15kg")
        while len(pedidos)>i:
            print(pedidos[i]["rut"],end=" ")
            print(pedidos[i]["cliente"],end=" ")
            print(pedidos[i]["direccion"],end=" ")
            print(pedidos[i]["comuna"],end=" ")
            print(pedidos[i]["cil.5kg"],end="    ")
            print(pedidos[i]["cil.15kg"],end=" ")
            print(pedidos[i]["Total"])
            i=i+1
    esperar_tecla()


def opcion3():
    i=0
    encontrado=0
    rut_bus=input("ingrese el rut que desea buscar: ")
    limpiar_pantalla()
    while i<len(pedidos):
        if pedidos[i]["rut"]==rut_bus:
            encontrado=1
            print(pedidos[i]["rut"],end=" ")
            print(pedidos[i]["cliente"],end=" ")
            print(pedidos[i]["direccion"],end=" ")
            print(pedidos[i]["comuna"],end=" ")
            print(pedidos[i]["cil.5kg"],end="    ")
            print(pedidos[i]["cil.15kg"],end=" ")
            print(pedidos[i]["Total"])
        i=i+1         
    if encontrado==0:
        print("No se ha encontrado el rut en los pedido")   
    esperar_tecla()



def opcion4():
    i=0
    limpiar_pantalla()
    print("comunas")
    print("1-Puente alto")
    print("2-Pintana")
    print("3-Pirque")
    comuna_bus=int(input("ingrese la opcion de la comuna para imprimir sus pedidos: "))
    if comuna_bus==1:
        busqueda="puente alto"
    elif comuna_bus==2:
        busqueda="pintana"
    else:
        busqueda="pirque"

    nombre_arch=input("Ingrese el nombre de los archivos: ")+".csv"
    with open(nombre_arch,"a",newline="") as archivo:
        escritor=csv.DictWriter(archivo,["rut","cliente","direccion","comuna","cil.5kg","cil.15kg","Total"])
        escritor.writeheader()
        while i<len(pedidos):
            if pedidos[i]["comuna"]==busqueda:
                escritor.writerow(pedidos[i])
            i=i+1
    limpiar_pantalla()
    print("Se ha logrado agregar con exitó")
    esperar_tecla()

def opcion5():
    limpiar_pantalla()
    print("Gracias por preferirnos y que tenga un buen dia")


def validar_rut():
    while True:
        try:
            rut=int(input("ingrese su rut (sin puntos,ni guion,ni digito verificador): "))
            if len(rut)==7 and len(rut)==8:
                return rut
            else:
                print("ERROR,el rut no es valido")
        except:
            print("Solo debe ingresar numero")

def validar_nombre():
    while True:
        nombre=input("ingrese su nombre:")
        if len(nombre)>3:
            return nombre
        else:
            print("ERROR, no se acepta un nombre tan corto")

def validar_direccion():
    while True:
        direccion=input("ingrese su direccion: ")
        if len(direccion)>3:
            return direccion
        else:
            print("ERROR, no se acepta una direccion tan corta")
    
def validar_comuna():
    while True:
        comuna=input("ingrese su comuna(puente alto - pintana - pirque): ") 
        if comuna.lower()=="puente alto":
           return comuna
        elif comuna.lower()=="pintana":
           return comuna
        elif comuna.lower()=="pirque":
           return comuna
        else:
           print("ERROR,comuna ingresada no es correcta")

def validar_cilindro5kg():
    while True:
        try:
            cinco_kg=int(input("ingrese la cantidad de cilindros de 5KG que desea: "))
            if cinco_kg>=0:
                return cinco_kg
            else:
                print("ERROR,la cantidad debe ser igual o mayor que 0,no se permite negativos")
        except:
            print("ERROR,solo se permiten numero")

def validar_cilindro15kg():
    while True:
        try:
            quince_kg=int(input("ingrese la cantidad de cilindros de 15KG que desea: "))
            if quince_kg>=0:
                return quince_kg
            else:
                print("ERROR,la cantidad debe ser igual o mayor que 0,no se permite negativos")
        except:
            print("ERROR,solo se permiten numero")



    