from engine.timetable_engine import generate
from output.timetable_console import display
from output.timetable_html import render_html

timetable = generate()

display(timetable)
render_html(timetable)
