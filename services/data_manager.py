import json
import os

BASE_DIR = "data"

def _ensure_file(file, default_data):
    path = os.path.join(BASE_DIR, file)
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default_data, f, indent=4)

def load(file):
    path = os.path.join(BASE_DIR, file)

    # Auto-create files if missing
    if file == "faculty.json":
        _ensure_file(file, {})
    elif file == "subjects.json":
        _ensure_file(file, {})
    elif file == "labs.json":
        _ensure_file(file, {})
    elif file == "batches.json":
        _ensure_file(file, ["A1", "A2", "A3"])

    with open(path, "r") as f:
        content = f.read().strip()
        if content == "":
            return {}
        return json.loads(content)

def save(file, data):
    path = os.path.join(BASE_DIR, file)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
