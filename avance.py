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
    question = input("¿Desea continuar? (s/n): ").lower()
    nombre = input("Ingrese el nombre del estudiante: ").lower().split()
    return question, nombre

def salir():
    print("""Desea continuar con el programa?
    1. Si
    2. No
            """)
    op = int(input("Ingrese una opción: "))
    while not op in [1, 2]:
        op = int(input("Ingrese una opción valida para continuar: "))
    return op
        
while True:
    menu()
    opcion = int(input("Ingrese una opcion: "))

    while not opcion in [0, 1, 2, 3, 4]:
        opcion = int(input("Ingrese una opción valida para continuar: "))
        
    if opcion == 1:
        os.system('cls')
        nombre = []
        lista_inasistencias = 0
        instructor = input("Ingrese el nombre del instructor: ").lower()
        print("----------------------------")
        horas = int(input("Ingrese la cantidad de horas de la clase: "))
        print("----------------------------")            
        nombre = input("Ingrese el nombre del estudiante: ").lower().split()
        lista_inasistencias += 1
        os.system('cls')
        print(f"La inasistencia de {nombre} ha sido agregada. Total de inasistencias: {lista_inasistencias}")
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
        nombre = input("Ingrese el nombre del estudiante que desea eliminar la inasistencia: ").lower()
        print(f"La inasistencia de {nombre} ha sido eliminada.")
        print("----------------------------")
        salir()

    elif opcion == 0:
        print("Saliendo del programa...")
        break
    elif opcion == 2:
        nombre = input("Ingrese el nombre del estudiante que desea editar la inasistencia: ").lower()
      
