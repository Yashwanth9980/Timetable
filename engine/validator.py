def validate(timetable):
    faculty_usage = set()

    for day, slots in timetable.items():
        for slot, value in slots.items():
            if value in (None, "BREAK"):
                continue
            if "(" in value:
                faculty = value.split("(")[-1].replace(")", "")
                key = (day, slot, faculty)
                if key in faculty_usage:
                    raise Exception(f"Faculty conflict: {faculty} on {day} {slot}")
                faculty_usage.add(key)
