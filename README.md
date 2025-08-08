# Aplicación de tareas

Pequeña aplicación para gestionar tareas con persistencia en un archivo `tasks.json`. 
Incluye una interfaz de línea de comandos y una interfaz gráfica construida con Tkinter.

## Requisitos

- Python 3.8 o superior

## Interfaz gráfica

Para lanzar la ventana gráfica:

```bash
python app.py
```

La ventana muestra las tareas con casillas para marcarlas como completadas, un campo 
para añadir nuevas tareas y botones para eliminar la tarea seleccionada o limpiar todas.

## Línea de comandos

También puedes gestionar las tareas desde la línea de comandos. Ejemplos:

```bash
python main.py add "Comprar pan"
python main.py list
python main.py done 1
python main.py remove 1
python main.py clear
```

Las tareas se guardan en el archivo `tasks.json` en el mismo directorio.

## Pruebas

Para ejecutar las pruebas básicas (opcionales):

```bash
pytest
```
