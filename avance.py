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
    pregun = input("""¿Desea continuar? 
1.si
2.no 
    """).lower()
    return pregun

def salir():
    print("""Desea continuar con el programa?
    1. Si
    2. No
            """)
    op = int(input("Ingrese una opción: "))
    while not op in [1, 2]:
        op = int(input("Ingrese una opción valida para continuar: "))
    return op

nombre = ["jor", "jose", "juan"]
instructor = ["keke", "juaan", "jose"]
horas_clase = [222, 333, 444]

while True:
    menu()
    opcion = int(input("Ingrese una opcion: "))

    while not opcion in [0, 1, 2, 3, 4]:
        opcion = int(input("Ingrese una opción valida para continuar: "))
        
    if opcion == 1:
        os.system('cls')       
        lista_inasistencias = 0
        nommbre_instructor = input("Ingrese el nombre del instructor: ").lower()
        instructor.append(nommbre_instructor)
        print("----------------------------")
        horas = int(input("Ingrese la cantidad de horas de la clase: "))
        horas_clase.append(horas)
        print("----------------------------")            
        nombre_estudi = input("Ingrese el nombre del estudiante: ").lower()
        nombre.append(nombre_estudi)
        lista_inasistencias += 1
        os.system('cls')
        print(f"La inasistencia de {nombre_estudi} ha sido agregada. Total de inasistencias: {lista_inasistencias}")
        print("----------------------------")
        print(f"La inasistencia la registra el instructor {nommbre_instructor}")
        print("-------------------------")
        print(f"Cantidad de horas de la inasistencia: {horas}")
        print("-------------------------") 
        op = salir()  
        if op == 1:
            continue
        elif op == 2:
            print("Saliendo del programa...")
            break


    elif opcion == 2:
        os.system('cls')
        print("         LISTA INASISTENCIAS")
        print(" Nombre     |    Instructor   |   Horas")
        for i in range(len(nombre)):
            lugar = i + 1
            print(f"{lugar}. {nombre[i]}           {instructor[i]}             {horas_clase[i]}")
        posi = int(input("Ingrese el índice del estudiante que desea editar: "))
        posi = posi - 1
        nombre_nuevo = input("Ingrese el nuevo nombre del estudiate: ")
        instructor_nuevo = input("Ingrese el nuevo instructor: ")
        horas_nuevo = input("Ingrese las nuevas horas de clase: ")
        nombre[posi] = nombre_nuevo
        instructor[posi] = instructor_nuevo
        horas_clase[posi] = horas_nuevo
        for i in range(len(nombre)):
            lugar = i + 1
            print(f"{lugar}. {nombre[i]}           {instructor[i]}             {horas_clase[i]}")
        input("Presione Enter para volver al Menu")

    elif opcion == 3:
        os.system('cls')
        print("         LISTA INASISTENCIAS")
        print(" Nombre     |    Instructor   |   Horas")
        for i in range(len(nombre)):
            lugar = i + 1
            print(f"{lugar}. {nombre[i]}           {instructor[i]}             {horas_clase[i]}")
        posi = int(input("Ingrese el índice del estudiante que desea eliminar: "))
        posi = posi - 1
        del nombre[posi]
        del instructor[posi]
        del horas_clase[posi]
        print("         LISTA INASISTENCIAS")
        print(" Nombre     |    Instructor   |   Horas")
        for i in range(len(nombre)):
            lugar = i + 1
            print(f"{lugar}. {nombre[i]}           {instructor[i]}             {horas_clase[i]}")
        posi = int(input("Ingrese el índice del estudiante que desea eliminar: "))

    elif opcion == 0:
        print("Saliendo del programa...")
        break
    elif opcion == 2:
        nombre = input("Ingrese el nombre del estudiante que desea editar la inasistencia: ").lower()
      
