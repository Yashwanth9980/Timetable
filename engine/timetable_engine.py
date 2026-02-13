from config.constants import DAYS, TIME_SLOTS, BREAK_SLOTS
from engine.lab_allocator import allocate_labs
from engine.theory_allocator import allocate_theory
from engine.validator import validate

def generate():
    timetable = {d: {s: None for s in TIME_SLOTS} for d in DAYS}

    for d in DAYS:
        for b in BREAK_SLOTS:
            timetable[d][b] = "BREAK"

    allocate_labs(timetable)
    allocate_theory(timetable)
    validate(timetable)

    return timetable
