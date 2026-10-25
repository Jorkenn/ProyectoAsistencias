import time
import os
from datetime import datetime

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
 Nombre     |     ficha      |    Instructor   |   Horas   |        Fecha         |       Justificacion       """)
    for i in range(len(nombre)):
        lugar = i + 1
        print(f"{lugar}. {nombre[i]}        {fichas[i]}           {instructor[i]}             {horas_clase[i]}          {fecha[i].strftime("%d/%m/%Y")}            {justificaciones[i]}")

def posicion(p="editar"):
    cantidad = len(nombre)
    posi = correccion(f"\nIngrese el índice del estudiante que desea {p}: ")
    while posi > cantidad or posi <= 0:
        estudiantes()
        print("\nIngrese un indice valido.") 
        posi = correccion(f"Ingrese el índice del estudiante que desea {p}: ")
    return posi

def pregunta(d = "¿Desea continuar?", s = "", o = "No"):
    print(f"""\n{d} {s}
1.Si
2.{o} 
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
            while cosa < 0:
                print("Ingrese un numero valido")
                cosa = int(input(op))
            return cosa
        except ValueError:
            print("Opción inválida, introduce un número. \n")

def correccion_fecha():
    while True:
        fecha_texto = input("Introduce una fecha (formato DD/MM/YYYY): ")
        try:
            # Convierte el texto en fecha
            fecha_objeto = datetime.strptime(fecha_texto, "%d/%m/%Y")
            return fecha_objeto
        except ValueError:
            print("La fecha es invalida. Usa DD/MM/YYYY.")

def corregir_texto(mensaje):
    while True:
        texto = input(mensaje).strip().lower()

        if texto == "":
            print("El texto no puede estar vacío")
        else:
            return texto
            
nombre = []
instructor = []
horas_clase = [] 
fecha = []
justificaciones = []
fichas = []

while True:
    menu()
    opcion = correccion()
    while not opcion in [0, 1, 2, 3, 4]:
        menu()
        opcion = correccion(op = "Ingrese una opcion valida para continuar: ")
    if opcion == 1:
        titulo()
        nombre_estudi = corregir_texto("Ingrese el nombre del estudiante: ")
        ficha = correccion(op = "Ingrese la ficha del estudiante: ")              
        nombre_instructor = corregir_texto("Ingrese el nombre del instructor: ")
        horas = correccion(op = "Ingrese la cantidad de horas de la clase: ")
        fechas = correccion_fecha()
        nombre.append(nombre_estudi)
        fichas.append(ficha)
        instructor.append(nombre_instructor)
        horas_clase.append(horas)
        fecha.append(fechas)
        justi = pregunta(d="¿El estudiante tiene justificacion?")
        while not justi in [1,2]:
            estudiantes()
            justi = pregunta(s = "Seleccione un numero")
        if justi == 1:
            justificacion = corregir_texto("\nIngrese la justificacion: \n")
            justificaciones.append(justificacion)
        elif justi == 2:
            justificaciones.append("No tiene")
        cambio() 
        input("Presione Enter para volver al Menu")

    elif opcion == 2:
        if nombre == []:
            input("No se encuentran inasistencias. \nPresione ENTER para volver al Menu")   
            continue
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
            nombre_nuevo = corregir_texto("Ingrese el nuevo nombre del estudiate: ")
            ficha_nueva = correccion(op = "Ingrese la nueva ficha: ")
            instructor_nuevo = corregir_texto("Ingrese el nuevo instructor: ")
            horas_nuevo = correccion(op = "Ingrese la nueva cantidad de horas de la clase: ")
            fecha_nueva = correccion_fecha()
            justificacion_nueva = corregir_texto("Ingrese justificacion nueva: ")
            nombre[posi] = nombre_nuevo
            fichas[posi] = ficha_nueva
            instructor[posi] = instructor_nuevo
            horas_clase[posi] = horas_nuevo
            fecha[posi] = fecha_nueva
            justificaciones[posi] = justificacion_nueva
            cambio(c="editada")
            input("Presione Enter para volver al Menu")
        elif op == 2:
            continue
        

    elif opcion == 3:
        if nombre == []:
            input("No se encuentran inasistencias. \nPresione ENTER para volver al Menu")   
            continue
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
            del fichas[posi]
            del instructor[posi]
            del horas_clase[posi]
            del fecha[posi]
            del justificaciones[posi]
            cambio(c="eliminada")

            input("Presione Enter para volver al Menu")
        elif op == 2:
            continue


    elif opcion == 4:
        os.system('cls')
        escoge = pregunta(d="¿Desea ver la lista completa de inasistencias?", o = "Consultar estudiantes +3 inasistencias")
        if escoge == 1:
            estudiantes()
            print(f"\nInasistencias totales: {len(nombre)}")
            input("\nPresione Enter para volver al Menu")
        else:
            os.system('cls')
            print("""        =============================
          CANTIDAD DE INASISTENCIAS
        =============================
nombre    |    faltas""")
            encontrado = False

            for estudi in set(nombre):
                faltas = nombre.count(estudi)
                if faltas >= 3:
                    print(f"{estudi}           {faltas}")
                    encontrado = True
            if encontrado == False:
                print("No hay estudiantes con 3 o más inasistencias.")
            input("\nPresione Enter para volver al menu")

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
