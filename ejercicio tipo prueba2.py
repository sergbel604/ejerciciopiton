import csv
lista=[]
jugadores=[]
def menu():
    print("")
    print("-"*150)
    print(".-.-.-.-.-.- J U G A D O R E S     D E L    N I U P I    Q U E    H A N    A N O T A D O    G O L E S -.-.-.-.-.-.")
    print("-"*150)
    print("")
    print("1.- Agregar jugador")
    print("2.- Listar jugadores")
    print("3.- Imprimir datos del jugador")
    print("4.- Eliminar jugador")
    print("5.- Estadisticas")
    print("6.- Generar bbdd")
    print("7.- cargar datos desde archivo")
    print("0.- Salir")

def jugadorcitos(list):
    for x in list:
        print("Numero: ",x[0]," Nombre: ",x[1]," Goles: ",x[2]," Clasificación: ",x[3])

def eliminar(list):
    for x in list:
        if num==x[0]:
            lista.remove(x)

while True:
    amateur=False
    semi=False
    pro=False
    menu()
    op=int(input("Ingrese una opción: "))
    if op==1:
        print("")
        print("------ A G R E G A R   J U G A D O R ------")
        print("")
        num=int(input("Ingrese número de camiseta: "))
        nombre=input("Ingrese su nombre: ")
        goles=int(input("Ingrese sus goles: "))
        
        
        if goles>0 and goles<6:
            amateur=True
        elif goles>5 and goles<16:
            semi=True
        elif goles>16:
            pro=True
        if amateur:
            print("")
            print("AMATEUR")
            print("")
            clasificacion="amateur"
        if semi:
            print("")
            print("SEMI")
            print("")
            clasificacion="semi"
        if pro:
            print("")
            print("PRO")
            print("")
            clasificacion="pro"
        jugadores=[num,nombre,goles,clasificacion]
        lista.append(jugadores)

    elif op==2:
        print("")
        print("------ L I S T A    D E    J U G A D O R E S ------")
        print("")
        jugadorcitos(lista)
    elif op==3:
        encontrado=False
        print("")
        print("------ D A T O S   D E   J U G A D O R E S ------")
        print("")
        num=int(input("Ingrese número de camiseta: "))
        for i in lista:
            if num==i[0]:
                encontrado=True
                print("")
                print("-"*150)
                print("Numero: ",i[0]," Nombre: ",i[1]," Goles: ",i[2]," Clasificación: ",i[3])
                print("-"*150)
        if encontrado==False:
            print("No existe en la base de datos")
    elif op==4:
        encontrado=False
        print("")
        print("------ E L I M I N A R   J U G A D O R ------")
        print("")
        num=int(input("Ingrese número de camiseta: "))
        for i in lista:
            if num==i[0]:
                print("")
                print("-"*150)
                print("Numero: ",i[0]," Nombre: ",i[1]," Goles: ",i[2]," Clasificación: ",i[3])
                print("-"*150)

                while True:      #minimenu para verificar q se quiere eliminar
                    print("1.- eliminar jugador")
                    print("0.- volver al menú")
                    op2=int(input("Ingresa una opción: "))
                    if op2==1:
                        eliminar(lista)
                        break
                    elif op2==0:
                        print("")
                        print("Volviendo al menú")
                        print("")
                        break
    elif op==5:
        mayor=None
        print("")
        print("------ E S T A D Í S T I C A S ------")
        print("")
        acum=0
        elementos=len(lista)
        for i in lista:
            acum=i[2]+acum
            promedio=acum/elementos
            mayor_goles = max(i[2] for i in lista)
        print("Promedio de goles: ",promedio)
        print("Mayor cantidad de goles: ",mayor_goles)
    elif op==6:
        print("")
        print("------ G E N E R A R    B B D D ------")
        print("")
        with open('bbdd_jugadores','w',newline='')as bbdd_jugadores:
            escritor_csv=csv.writer(bbdd_jugadores)
            escritor_csv.writerows(lista) 
        print("")
        print("Bbdd generada")
        print("")
    elif op==7:
        print("")
        print("------ C A R G A R    B B D D ------")
        print("")
        with open('bbdd_jugadores','r',newline='')as bbdd_jugadores:
            lector_csv=csv.reader(bbdd_jugadores)
            for fila in lector_csv:
                lista.append(fila)
        print("")
        print("Bbdd cargada")
        print("")
    elif op==0:
        print("")
        print("Chao puto")
        print("")
        break
    else:
        print("")
        print("Opción inválida")
        print("")
