import tkinter as tk
from tkinter import messagebox
import main


class TodoApp:
    """Interfaz gráfica para la aplicación de tareas."""

    def __init__(self, root):
        self.root = root
        root.title("Lista de tareas")
        self.selected_task_id = None

        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(root)
        self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)

        add_btn = tk.Button(root, text="Agregar", command=self.add_task)
        add_btn.pack(padx=10, pady=(0, 10))

        btn_frame = tk.Frame(root)
        btn_frame.pack(padx=10, pady=(0, 10))
        del_btn = tk.Button(btn_frame, text="Eliminar seleccionada", command=self.remove_selected)
        del_btn.pack(side=tk.LEFT, padx=5)
        clear_btn = tk.Button(btn_frame, text="Limpiar todas", command=self.clear_all)
        clear_btn.pack(side=tk.LEFT, padx=5)

        self.refresh_tasks()

    def refresh_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        tasks = main.load_tasks()
        self.task_vars = {}
        for task in tasks:
            task_id = task["id"]
            var = tk.BooleanVar(value=task["done"])
            cb = tk.Checkbutton(
                self.tasks_frame,
                text=task["text"],
                variable=var,
                command=lambda tid=task_id, v=var: self.toggle_done(tid, v),
                anchor="w",
            )
            cb.pack(fill=tk.X, anchor="w")
            cb.bind("<Button-1>", lambda e, tid=task_id: self.select_task(tid))
            self.task_vars[task_id] = var

    def select_task(self, task_id):
        self.selected_task_id = task_id

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")
            return
        tasks = main.load_tasks()
        next_id = max((t["id"] for t in tasks), default=0) + 1
        tasks.append({"id": next_id, "text": text, "done": False})
        main.save_tasks(tasks)
        self.entry.delete(0, tk.END)
        self.refresh_tasks()

    def toggle_done(self, task_id, var):
        tasks = main.load_tasks()
        for t in tasks:
            if t["id"] == task_id:
                t["done"] = bool(var.get())
                break
        main.save_tasks(tasks)
        # no need to refresh; checkbox already reflects state

    def remove_selected(self):
        if self.selected_task_id is None:
            messagebox.showinfo("Info", "Seleccione una tarea para eliminar.")
            return
        tasks = main.load_tasks()
        tasks = [t for t in tasks if t["id"] != self.selected_task_id]
        main.save_tasks(tasks)
        self.selected_task_id = None
        self.refresh_tasks()

    def clear_all(self):
        if messagebox.askyesno("Confirmar", "¿Eliminar todas las tareas?"):
            main.save_tasks([])
            self.selected_task_id = None
            self.refresh_tasks()


def run():
    root = tk.Tk()
    TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    run()
