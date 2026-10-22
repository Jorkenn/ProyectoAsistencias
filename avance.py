import time
import os
def menu():
    os.system('cls')    
    print("""
Menu
1. Agregar inasistencia
2. Editar inasistencia
3. Eliminar inasistencia
4. Consultar inasistencias
0. Salir
""")

def pregunta():
    pregun = input("¿Desea continuar? (s/n): ").lower()
    return pregun

def salir():
    print("""Desea continuar con el programa? Responder con numeros
    1. Si
    2. No
            """)
    op = int(input("Ingrese una opción: "))
    while not op in [1, 2]:
        op = int(input("Ingrese una opción valida para continuar: "))
    return op

nombre = [0]

while True:
    menu()
    opcion = int(input("Ingrese una opcion: "))

    while not opcion in [0, 1, 2, 3, 4]:
        opcion = int(input("Ingrese una opción valida para continuar: "))
        
    if opcion == 1:
        os.system('cls')       
        lista_inasistencias = 0
        instructor = input("Ingrese el nombre del instructor: ").lower()
        print("----------------------------")
        horas = int(input("Ingrese la cantidad de horas de la clase: "))
        print("----------------------------")            
        nombre_estudi = input("Ingrese el nombre del estudiante: ").lower().split()
        nombre.append(nombre_estudi)
        lista_inasistencias += 1
        os.system('cls')
        print(f"La inasistencia de {nombre_estudi} ha sido agregada. Total de inasistencias: {lista_inasistencias}")
        print("----------------------------")
        print(f"La inasistencia la registra el instructor {instructor}")
        print("-------------------------")
        print(f"Cantidad de horas de la inasistencia: {horas}")
        print("-------------------------") 
        op = salir()  
        if op == 1:
            continue
        elif op == 2:
            print("Saliendo del programa...")
            break
        
    elif opcion == 3:
        os.system('cls')
        print(nombre)
        nombres = input("Ingrese el nombre del estudiante que desea eliminar la inasistencia: ").lower()
        while nombres not in nombre:
            print("El estudiante no se encuentra en la lista.")
            escoger =pregunta()
            while not escoger in ["s", "n"]:
                escoger = input("Ingrese una opción valida para continuar: ").lower()
            if escoger == "s":
                nombres = input("Ingrese el nombre del estudiante que desea eliminar la inasistencia: ").lower()
            elif escoger == "n":
                print("Saliendo del programa...")
                break 
        if escoger == "n":
            print()
        else:    
            nombre.remove(nombres)
            print(nombre)
            print(f"La inasistencia de {nombres} ha sido eliminada.")
            print("----------------------------")
            op = salir()  
            if op == 1:
                continue
            elif op == 2:
                print("Saliendo del programa...")
                break

    elif opcion == 0:
        print("Saliendo del programa...")
        break

    elif opcion == 2:
        print("¿Que va editar en la inasitencias? 1.Agregar inasitencias 2.Eliminar inasistencias ")
        n = int(input("Ingrese la opcion en numero"))
        nombre = input("Ingrese el nombre del estudiante que desea editar la inasistencia: ").lower()
        if n == 1:
            numero = int(input("¿Cuantas inasistencias va registrar?"))
            print(f"La cantidad de inasitencias ({numero}) a sido registrado a el aprendiz {nombre}")   
