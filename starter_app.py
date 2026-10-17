import json
import sys
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.json")


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: starter_app.py add <task> | list | delete <task#>")

    command = sys.argv[1].lower()
    tasks = json.loads(TASKS_FILE.read_text(encoding="utf-8")) if TASKS_FILE.exists() else []
    if command not in {"add", "list", "delete"}:
        raise SystemExit('Unknown command. Use "add", "list", or "delete".')
    if command == "add":
        task = " ".join(sys.argv[2:]).strip()
        if not task:
            raise SystemExit("Please provide a task to add.")
        tasks.append(task)
        print(f"Added task: {task}")
    elif command == "list":
        print("\n".join(f"{i}. {task}" for i, task in enumerate(tasks, 1)) or "No tasks.")
        return
    elif command == "delete":
        number = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdecimal() else 0
        if not 1 <= number <= len(tasks):
            raise SystemExit("Provide a valid task number.")
        print(f"Deleted task: {tasks.pop(number - 1)}")
    TASKS_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
