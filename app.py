tareas = []

def mostrar_tareas():
    if not tareas:
        print("\nNo hay tareas registradas.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            estado = "✓" if tarea["completada"] else "○"
            print(f"{i}. [{estado}] {tarea['nombre']}")

def agregar_tarea():
    nombre = input("\nEscribe la nueva tarea: ").strip()
    if nombre:
        tareas.append({"nombre": nombre, "completada": False})
        print("Tarea agregada correctamente.")
    else:
        print("La tarea no puede estar vacía.")

def completar_tarea():
    mostrar_tareas()
    if tareas:
        try:
            numero = int(input("\nNúmero de la tarea completada: "))
            if 1 <= numero <= len(tareas):
                tareas[numero - 1]["completada"] = True
                print("Tarea marcada como completada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Debes ingresar un número.")

def eliminar_tarea():
    mostrar_tareas()
    if tareas:
        try:
            numero = int(input("\nNúmero de la tarea que deseas eliminar: "))
            if 1 <= numero <= len(tareas):
                tareas.pop(numero - 1)
                print("Tarea eliminada correctamente.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Debes ingresar un número.")

while True:
    print("\n===== LISTA DE TAREAS =====")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("Aplicación finalizada.")
        break
    else:
        print("Opción inválida.")