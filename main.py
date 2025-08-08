import argparse
import json
import os

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(text):
    tasks = load_tasks()
    next_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": next_id, "text": text, "done": False})
    save_tasks(tasks)
    print(f"Tarea {next_id} agregada.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No hay tareas.")
        return
    for t in tasks:
        status = "✔" if t["done"] else "✘"
        print(f"{t['id']}: [{status}] {t['text']}")

def mark_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            if t["done"]:
                print("La tarea ya está completada.")
            else:
                t["done"] = True
                save_tasks(tasks)
                print(f"Tarea {task_id} marcada como completada.")
            return
    print(f"Tarea con ID {task_id} no encontrada.")

def remove_task(task_id):
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks.pop(i)
            save_tasks(tasks)
            print(f"Tarea {task_id} eliminada.")
            return
    print(f"Tarea con ID {task_id} no encontrada.")

def clear_tasks():
    save_tasks([])
    print("Todas las tareas fueron eliminadas.")

def main():
    parser = argparse.ArgumentParser(description="Aplicación de tareas por línea de comandos.")
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add", help="Agregar una nueva tarea")
    parser_add.add_argument("text", help="Texto de la tarea")

    subparsers.add_parser("list", help="Listar tareas")

    parser_done = subparsers.add_parser("done", help="Marcar una tarea como completada")
    parser_done.add_argument("id", type=int, help="ID de la tarea")

    parser_remove = subparsers.add_parser("remove", help="Eliminar una tarea")
    parser_remove.add_argument("id", type=int, help="ID de la tarea")

    subparsers.add_parser("clear", help="Eliminar todas las tareas")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.text)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.id)
    elif args.command == "remove":
        remove_task(args.id)
    elif args.command == "clear":
        clear_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
