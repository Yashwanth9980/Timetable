from services.data_manager import load, save

def add_faculty(code, name, max_hours):
    faculty = load("faculty.json")
    if code in faculty:
        raise Exception("Faculty already exists")
    faculty[code] = {"name": name, "max_hours": max_hours}
    save("faculty.json", faculty)

def update_faculty(code, name, max_hours):
    faculty = load("faculty.json")
    faculty[code]["name"] = name
    faculty[code]["max_hours"] = max_hours
    save("faculty.json", faculty)

def delete_faculty(code):
    subjects = load("subjects.json")
    for s in subjects.values():
        if s["faculty"] == code:
            raise Exception("Faculty assigned to subject")
    faculty = load("faculty.json")
    faculty.pop(code, None)
    save("faculty.json", faculty)
