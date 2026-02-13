from services.data_manager import load, save

def add_subject(code, name, faculty, hours, stype):
    subjects = load("subjects.json")
    subjects[code] = {
        "name": name,
        "faculty": faculty,
        "hours": hours,
        "type": stype
    }
    save("subjects.json", subjects)

def update_subject(code, name, faculty, hours, stype):
    subjects = load("subjects.json")
    subjects[code] = {
        "name": name,
        "faculty": faculty,
        "hours": hours,
        "type": stype
    }
    save("subjects.json", subjects)

def delete_subject(code):
    subjects = load("subjects.json")
    subjects.pop(code, None)
    save("subjects.json", subjects)
