from flask import Flask, render_template, request, redirect, url_for
from engine.timetable_engine import generate
from services.faculty_service import add_faculty, delete_faculty
from services.subject_service import add_subject, delete_subject
from services.lab_service import add_lab, delete_lab
from services.data_manager import load
from config.constants import TIME_SLOTS

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/faculty", methods=["GET", "POST"])
def faculty():
    if request.method == "POST":
        add_faculty(
            request.form["code"],
            request.form["name"],
            int(request.form["hours"])
        )
        return redirect(url_for("faculty"))

    faculty = load("faculty.json")
    return render_template("faculty.html", faculty=faculty)

@app.route("/subject", methods=["GET", "POST"])
def subject():
    if request.method == "POST":
        add_subject(
            request.form["code"],
            request.form["name"],
            request.form["faculty"],
            int(request.form["hours"]),
            request.form["type"]
        )
        return redirect(url_for("subject"))

    subjects = load("subjects.json")
    faculty = load("faculty.json")
    return render_template("subject.html", subjects=subjects, faculty=faculty)

@app.route("/lab", methods=["GET", "POST"])
def lab():
    if request.method == "POST":
        add_lab(
            request.form["lab_id"],
            request.form["name"],
            request.form["room"],
            ["A1", "A2", "A3"]
        )
        return redirect(url_for("lab"))

    labs = load("labs.json")
    return render_template("lab.html", labs=labs)

@app.route("/generate")
def generate_tt():
    timetable = generate()
    return render_template(
        "timetable.html",
        timetable=timetable,
        time_slots=TIME_SLOTS
    )

if __name__ == "__main__":
    app.run(debug=True)
