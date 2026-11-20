import json
import os

DEFAULT_PATH = os.environ.get("TASKLIST_FILE", "tasks.json")


def load(path=DEFAULT_PATH):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return json.load(f)


def save(tasks, path=DEFAULT_PATH):
    with open(path, "w") as f:
        json.dump(tasks, f, indent=2)


def add(title, path=DEFAULT_PATH):
    tasks = load(path)
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    save(tasks, path)
    return task
