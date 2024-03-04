Nombre del Proyecto: Sistema de Gestión de Tareas

Descripción:
Desarrolla un sistema de gestión de tareas que permita a los usuarios organizar sus actividades diarias, establecer prioridades y realizar un seguimiento del progreso.

Requisitos:

    Interfaz de Usuario:
        El sistema debe tener una interfaz de línea de comandos (CLI) para la interacción con el usuario.
        Debe permitir al usuario agregar nuevas tareas, marcar tareas como completadas, eliminar tareas y ver la lista de tareas pendientes.

    Funcionalidades:
        Agregar tarea: El usuario debe poder agregar una nueva tarea proporcionando un título, una descripción y una fecha de vencimiento (opcional).
        Marcar tarea como completada: El usuario debe poder marcar una tarea como completada.
        Eliminar tarea: El usuario debe poder eliminar una tarea de la lista.
        Ver lista de tareas: El usuario debe poder ver la lista de todas las tareas, mostrando su título, descripción, estado (pendiente o completada) y fecha de vencimiento (si está definida).
        Filtrar tareas: El usuario debe poder filtrar las tareas según su estado (pendiente/completada) o fecha de vencimiento.
        Guardar y cargar datos: El sistema debe ser capaz de guardar y cargar los datos de las tareas en un archivo para que la información persista entre sesiones.

    Validaciones:
        Validar la entrada del usuario para evitar errores y asegurar que los datos proporcionados sean válidos.
        Manejar posibles errores como la falta de archivos de datos o problemas de lectura/escritura.

    Opcionales:
        Implementar una interfaz gráfica de usuario (GUI) usando bibliotecas como Tkinter o PyQt para mejorar la experiencia del usuario.
        Agregar funcionalidades avanzadas como recordatorios de tareas próximas, clasificación por categorías, etc.

Tecnologías sugeridas:

    Python 3.x
    Para la persistencia de datos, puedes utilizar archivos de texto plano, formato CSV o incluso bases de datos SQLite si deseas explorar un enfoque más avanzado.
    Para la interfaz de línea de comandos, puedes usar la biblioteca estándar argparse.
    Para la interfaz gráfica de usuario, puedes explorar bibliotecas como Tkinter o PyQt.
