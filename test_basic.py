import main


def setup_tmp(tmp_path):
    main.TASKS_FILE = str(tmp_path / "tasks.json")


def test_add_and_done(tmp_path, capsys):
    setup_tmp(tmp_path)

    main.add_task("Tarea de prueba")
    out = capsys.readouterr().out
    assert "Tarea 1 agregada" in out

    main.list_tasks()
    out = capsys.readouterr().out
    assert "1: [✘] Tarea de prueba" in out

    main.mark_done(1)
    out = capsys.readouterr().out
    assert "marcada como completada" in out

    main.list_tasks()
    out = capsys.readouterr().out
    assert "1: [✔] Tarea de prueba" in out
