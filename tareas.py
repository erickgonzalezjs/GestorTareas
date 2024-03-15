from datetime import datetime

tareas = []
tareas_importantes = []

def agregar_tarea():
    """
    Agrega una nueva tarea a la lista de tareas.
    Solicita al usuario la descripción y la fecha límite de la tarea.
    """
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_limite = input("Ingrese la fecha límite (formato YYYY-MM-DD): ")
    try:
        tarea = {
            "descripcion": descripcion,
            "fecha_limite": datetime.strptime(fecha_limite, "%Y-%m-%d"),
            "estado": "pendiente",
        }
        tareas.append(tarea)
        print("Tarea agregada exitosamente.")
    except ValueError:
        print("Formato de fecha incorrecto. Use el formato YYYY-MM-DD.")

def listar_tareas():
    """
    Lista todas las tareas almacenadas, incluyendo su descripción, fecha límite y estado.
    """
    print("**Tareas normales**")
    if not tareas:
        print("No hay tareas normales.")
    for tarea in tareas:
        print(f"ID: {tareas.index(tarea)}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Fecha límite: {tarea['fecha_limite'].strftime('%Y-%m-%d')}")
        print(f"Estado: {tarea['estado']}")
        print("---")

def completar_tarea():
    """
    Marca una tarea como completada.
    Solicita al usuario el ID de la tarea correspondiente.
    """
    if not tareas:
        print("No hay tareas para completar.")
        return
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
        if 0 <= id_tarea < len(tareas):
            tareas[id_tarea]["estado"] = "completada"
            print("Tarea completada.")
        else:
            print("ID de tarea fuera de rango.")
    except ValueError:
        print("ID de tarea debe ser un número entero.")

def eliminar_tarea():
    """
    Elimina una tarea de la lista.
    Solicita al usuario el ID de la tarea correspondiente.
    """
    if not tareas:
        print("No hay tareas para eliminar.")
        return
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
        if 0 <= id_tarea < len(tareas):
            del tareas[id_tarea]
            print("Tarea eliminada.")
        else:
            print("ID de tarea fuera de rango.")
    except ValueError:
        print("ID de tarea debe ser un número entero.")

def menu_principal():
    """
    Función principal que muestra el menú y gestiona las opciones del usuario.
    """
    while True:
        print("**Sistema de gestión de tareas**")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea()
        elif opcion == '2':
            listar_tareas()
        elif opcion == '3':
            completar_tarea()
        elif opcion == '4':
            eliminar_tarea()
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")

    print("¡Hasta luego!")

# Llama a la función del menú principal
menu_principal()
