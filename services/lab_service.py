from services.data_manager import load, save

def add_lab(lab_id, name, room):
    labs = load("labs.json")
    labs[lab_id] = {
        "name": name,
        "room": room,
        "batches": ["A1", "A2", "A3"]
    }
    save("labs.json", labs)

def update_lab(lab_id, name, room):
    labs = load("labs.json")
    labs[lab_id]["name"] = name
    labs[lab_id]["room"] = room
    save("labs.json", labs)

def delete_lab(lab_id):
    labs = load("labs.json")
    labs.pop(lab_id, None)
    save("labs.json", labs)
