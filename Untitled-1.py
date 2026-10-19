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
lista_inasistencias = []
opcion = int(input("Ingrese una opcion:"))

while not (opcion != 0 and opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4):
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
       