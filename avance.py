def menu():
        
    print("""
Menu
1. Agregar inasistencia
2. Editar inasistencia
3. Eliminar inasistencia
4. Consultar inasistencias
0. Salir
""")

menu()

lista_estudiantes = []
lista_inasistencias = 0
opcion = int(input("Ingrese una opcion:"))

while not opcion in [0, 1, 2, 3, 4]:
    opcion = int(input("Ingrese una opción valida para continuar: "))
    
    if opcion == 1:
        lista_estudiantes = input("Ingrese los nombres de los estudiantes separados por comas: ").lower().split(",")
        nombre = input("Ingrese el nombre del estudiante: ").lower()
        while nombre not in lista_estudiantes:
            nombre = input("Estudiante no encontrado. Ingrese un nombre válido: ").lower()
        lista_inasistencias += 1
        print(f"La inasistencia de {nombre} ha sido agregada. Total de inasistencias: {lista_inasistencias}")

    elif opcion == 0:
        print("Saliendo del programa...")
        break
