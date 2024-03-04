class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tarea '{task}' agregada correctamente.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index] += " - Completada"
            print(f"Tarea {index} marcada como completada.")
        else:
            print("Índice de tarea no válido.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print(f"Tarea {index} eliminada correctamente.")
        else:
            print("Índice de tarea no válido.")

    def show_tasks(self):
        if self.tasks:
            print("Lista de tareas:")
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")
        else:
            print("No hay tareas pendientes.")

def main():
    todo_list = ToDoList()
    while True:
        print("\n--- Menú ---")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Eliminar tarea")
        print("4. Ver tareas pendientes")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            task = input("Ingrese la nueva tarea: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Ingrese el índice de la tarea completada: "))
            todo_list.complete_task(index)
        elif choice == "3":
            index = int(input("Ingrese el índice de la tarea a eliminar: "))
            todo_list.delete_task(index)
        elif choice == "4":
            todo_list.show_tasks()
        elif choice == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
