from flask import Flask, render_template, request, redirect, url_for, flash
from services.data_manager import load
from services.faculty_service import add_faculty, update_faculty, delete_faculty
from services.subject_service import add_subject, update_subject, delete_subject
from services.lab_service import add_lab, update_lab, delete_lab
from engine.timetable_engine import generate
from config.constants import TIME_SLOTS

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/")
def index():
    return render_template("index.html")

# FACULTY
@app.route("/faculty", methods=["GET", "POST"])
def faculty():
    if request.method == "POST":
        try:
            add_faculty(request.form["code"], request.form["name"], int(request.form["hours"]))
            flash("Faculty added", "success")
        except Exception as e:
            flash(str(e), "error")
        return redirect(url_for("faculty"))
    return render_template("faculty.html", faculty=load("faculty.json"))

@app.route("/faculty/edit/<code>", methods=["GET", "POST"])
def edit_faculty(code):
    faculty = load("faculty.json")
    if request.method == "POST":
        update_faculty(code, request.form["name"], int(request.form["hours"]))
        flash("Faculty updated", "success")
        return redirect(url_for("faculty"))
    return render_template("faculty_edit.html", code=code, faculty=faculty[code])

@app.route("/faculty/delete/<code>", methods=["POST"])
def delete_faculty_route(code):
    try:
        delete_faculty(code)
        flash("Faculty deleted", "success")
    except Exception as e:
        flash(str(e), "error")
    return redirect(url_for("faculty"))

# SUBJECT
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
        flash("Subject added", "success")
        return redirect(url_for("subject"))
    return render_template("subject.html",
                           subjects=load("subjects.json"),
                           faculty=load("faculty.json"))

@app.route("/subject/edit/<code>", methods=["GET", "POST"])
def edit_subject(code):
    subjects = load("subjects.json")
    faculty = load("faculty.json")
    if request.method == "POST":
        update_subject(
            code,
            request.form["name"],
            request.form["faculty"],
            int(request.form["hours"]),
            request.form["type"]
        )
        flash("Subject updated", "success")
        return redirect(url_for("subject"))
    return render_template("subject_edit.html", code=code, subject=subjects[code], faculty=faculty)

@app.route("/subject/delete/<code>", methods=["POST"])
def delete_subject_route(code):
    delete_subject(code)
    flash("Subject deleted", "success")
    return redirect(url_for("subject"))

# LAB
@app.route("/lab", methods=["GET", "POST"])
def lab():
    if request.method == "POST":
        add_lab(request.form["lab_id"], request.form["name"], request.form["room"])
        flash("Lab added", "success")
        return redirect(url_for("lab"))
    return render_template("lab.html", labs=load("labs.json"))

@app.route("/lab/edit/<lab_id>", methods=["GET", "POST"])
def edit_lab(lab_id):
    labs = load("labs.json")
    if request.method == "POST":
        update_lab(lab_id, request.form["name"], request.form["room"])
        flash("Lab updated", "success")
        return redirect(url_for("lab"))
    return render_template("lab_edit.html", lab_id=lab_id, lab=labs[lab_id])

@app.route("/lab/delete/<lab_id>", methods=["POST"])
def delete_lab_route(lab_id):
    delete_lab(lab_id)
    flash("Lab deleted", "success")
    return redirect(url_for("lab"))

# TIMETABLE
@app.route("/generate")
def generate_tt():
    timetable = generate()
    return render_template("timetable.html", timetable=timetable, time_slots=TIME_SLOTS)

if __name__ == "__main__":
    app.run(debug=True)
