from jinja2 import Environment, FileSystemLoader
from config.constants import TIME_SLOTS
from services.data_manager import load

def render_html(timetable):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("timetable.html")

    subjects = load("subjects.json")
    course_faculty = {
        code: sub["faculty"] for code, sub in subjects.items()
    }

    html = template.render(
        timetable=timetable,
        time_slots=TIME_SLOTS,
        course_faculty=course_faculty
    )

    with open("timetable.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("✔ Timetable HTML generated: timetable.html")
