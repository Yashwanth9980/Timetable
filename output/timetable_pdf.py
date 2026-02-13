"""
PDF Output
"""

from reportlab.pdfgen import canvas

def generate_pdf(timetable, filename):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, "Timetable")
    # Add more drawing logic
    c.save()