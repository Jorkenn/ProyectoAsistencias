import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    limpiar_pantalla()
    print("""
--- MENÚ DE INASISTENCIAS ---
1. Agregar inasistencia
2. Editar inasistencia
3. Eliminar inasistencia
4. Consultar inasistencias
0. Salir
""")

def salir():
    print("\n¿Desea volver al menú principal?")
    print("1. Sí")
    print("2. No (Salir del programa)")
    op = int(input("Ingrese una opción: "))
    while op not in [1, 2]:
        op = int(input("Ingrese una opción válida: "))
    return op

inasistencias = [] 

while True:
    menu()
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Por favor ingrese un número.")
        input("Presione Enter para continuar...")
        continue

    if opcion not in [0, 1, 2, 3, 4]:
        input("Opción no válida. Presione Enter para continuar...")
        continue
        
    if opcion == 1: 
        limpiar_pantalla()       
        instructor = input("Ingrese el nombre del instructor: ").lower().strip()
        horas = int(input("Ingrese la cantidad de horas de la clase: "))
        nombre_estudi = input("Ingrese el nombre del estudiante: ").lower().strip()
        
        
        registro = {
            "estudiante": nombre_estudi,
            "instructor": instructor,
            "horas": horas
        }
        inasistencias.append(registro)
        
        limpiar_pantalla()
        print(f"La inasistencia de {nombre_estudi.title()} ha sido agregada.")
        print(f"Total de inasistencias registradas en el sistema: {len(inasistencias)}")
        print("----------------------------")
        
        if salir() == 2:
            print("Saliendo del programa...")
            break
            
    elif opcion == 2: # EDITAR
        limpiar_pantalla()
        if not inasistencias:
            print("No hay inasistencias registradas para editar.")
        else:
            estudiante_buscar = input("Ingrese el nombre del estudiante a editar: ").lower().strip()
            encontrado = False
            
            for registro in inasistencias:
                if registro["estudiante"] == estudiante_buscar:
                    encontrado = True
                    print(f"Registro actual: Instructor: {registro['instructor']}, Horas: {registro['horas']}")
                    nueva_hora = int(input("Ingrese la nueva cantidad de horas (o repita la actual): "))
                    registro["horas"] = nueva_hora
                    print("¡Inasistencia editada correctamente!")
                    break
                    
            if not encontrado:
                print("Estudiante no encontrado en los registros.")
                
        if salir() == 2:
            print("Saliendo del programa...")
            break

    elif opcion == 3: # ELIMINAR
        limpiar_pantalla()
        if not inasistencias:
            print("No hay inasistencias registradas para eliminar.")
        else:
            estudiante_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ").lower().strip()
            
            # Buscamos y eliminamos
            registros_previos = len(inasistencias)
            inasistencias = [r for r in inasistencias if r["estudiante"] != estudiante_eliminar]
            
            if len(inasistencias) < registros_previos:
                print(f"Las inasistencias de {estudiante_eliminar.title()} han sido eliminadas.")
            else:
                print("El estudiante no se encuentra en la lista.")
                
        if salir() == 2:
            print("Saliendo del programa...")
            break

    elif opcion == 4:
        limpiar_pantalla()
        print("--- LISTADO DE INASISTENCIAS ---")
        if not inasistencias:
            print("No hay registros actualmente.")
        else:
            for i, reg in enumerate(inasistencias, 1):
                print(f"{i}. Estudiante: {reg['estudiante'].title()} | Instructor: {reg['instructor'].title()} | Horas: {reg['horas']}")
        
        if salir() == 2:
            print("Saliendo del programa...")
            break

    elif opcion == 0: 
        print("Saliendo del programa...")
        break