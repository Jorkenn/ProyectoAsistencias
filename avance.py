import time
import os

def menu():
    os.system('cls')    
    print("""    =============================
    MENU DE REGISTRO INASISTENCIA
    =============================

1. Agregar inasistencia
2. Editar inasistencia
3. Eliminar inasistencia
4. Consultar inasistencias
0. Salir
""")

def titulo(t="AÑADIR"):
    os.system('cls')
    print(f"""    =============================
        {t} INASISTENCIA
    =============================""") 

def cambio(c = "añadida"):
    os.system('cls')    
    print(f"""    =============================
    MENU DE REGISTRO INASISTENCIA
    =============================

Inasistencia {c} correctamente
""")    

def estudiantes():
    os.system('cls')
    print("""    =============================
        LISTA INASISTENCIAS
    =============================
 Nombre     |    Instructor   |   Horas""")
    for i in range(len(nombre)):
        lugar = i + 1
        print(f"{lugar}. {nombre[i]}           {instructor[i]}             {horas_clase[i]}")

def posicion(p="editar"):
    cantidad = len(nombre)
    posi = correccion(f"\nIngrese el índice del estudiante que desea {p}: ")
    while posi > cantidad or posi <= 0:
        estudiantes()
        print("\nIngrese un indice valido.") 
        posi = correccion(f"Ingrese el índice del estudiante que desea {p}: ")
    return posi

def pregunta(s = ""):
    print(f"""\n¿Desea continuar? {s}
1.si
2.no 
""")
    op = correccion()
    while not op in [1, 2]:
        print("Escoja una opcion valida\n")
        op = correccion()
    return op

def salida():
    os.system('cls')
    print("""    =============================
    MENU DE REGISTRO INASISTENCIA
    =============================

Programa finalizado
""")

def correccion(op = "Ingrese una opcion: " ):
    while True:
        try:
            cosa = int(input(op))
            return cosa
    
        except ValueError:
            print("Opción inválida, introduce un número. \n")
            

nombre = ["jor", "jose", "juan"]
instructor = ["keke", "juaan", "jose"]
horas_clase = [222, 333, 444] 

while True:
    menu()
    opcion = correccion()
    while not opcion in [0, 1, 2, 3, 4]:
        menu()
        opcion = correccion(op = "Ingrese una opcion valida para continuar: ")
    if opcion == 1:
        titulo()
        nombre_estudi = input("Ingrese el nombre del estudiante: ").lower()              
        nombre_instructor = input("Ingrese el nombre del instructor: ").lower()
        horas = correccion(op = "Ingrese la cantidad de horas de la clase: ")
        instructor.append(nombre_instructor)
        horas_clase.append(horas)
        nombre.append(nombre_estudi)
        cambio() 
        input("Presione Enter para volver al Menu")


    elif opcion == 2:
        estudiantes()
        op = pregunta()
        while not op in [1,2]:
            estudiantes()
            op = pregunta(s = "Seleccione un numero") 
        if op == 1:
            estudiantes()
            posi = posicion()
            posi = posi - 1
            titulo(t="EDITAR")
            nombre_nuevo = input("Ingrese el nuevo nombre del estudiate: ")
            instructor_nuevo = input("Ingrese el nuevo instructor: ")
            horas_nuevo = correccion(op = "Ingrese la nueva cantidad de horas de la clase: ")
            nombre[posi] = nombre_nuevo
            instructor[posi] = instructor_nuevo
            horas_clase[posi] = horas_nuevo
            cambio(c="editada")
            input("Presione Enter para volver al Menu")
        elif op == 2:
            continue
        

    elif opcion == 3:
        estudiantes()
        op = pregunta()
        while not op in [1,2]:
            estudiantes()
            op = pregunta(s = "Seleccione un numero")
        if op == 1:
            estudiantes()
            lugar = posicion(p="eliminar")
            posi = lugar - 1
            del nombre[posi]
            del instructor[posi]
            del horas_clase[posi]
            cambio(c="eliminada")

            input("Presione Enter para volver al Menu")
        elif op == 2:
            continue


    elif opcion == 4:
        os.system('cls')
        estudiantes()
        print(f"\nInasistencias totales: {len(nombre)}")
        input("\nPresione Enter para volver al Menu")
        
    elif opcion == 0:
        salida()
        break

grupo = [
    ("""+==============+
|    Code by   |
|    JORDAN    |
|    JAINER    |
|    CARLOS    |
+==============+
 """,0.01)
 ]

for letra, tiempo in grupo:
    for let in letra:
        print(let, end="", flush=True)
        time.sleep(tiempo)
