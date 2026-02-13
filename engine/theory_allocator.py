from services.data_manager import load
from config.constants import DAYS, FIRST_HOUR, BREAK_SLOTS, TIME_SLOTS

def allocate_theory(timetable):
    subjects = load("subjects.json")
    theory_subjects = [
        (code, sub) for code, sub in subjects.items()
        if sub["type"] == "theory"
    ]

    faculty_busy = set()  # (day, slot, faculty)

    # -------------------------------------------------
    # STEP 1: Give each theory subject ONE first-hour slot in the week
    # -------------------------------------------------
    day_index = 0
    for code, sub in theory_subjects:
        faculty = sub["faculty"]

        for _ in range(len(DAYS)):
            day = DAYS[day_index % len(DAYS)]
            day_index += 1

            if timetable[day][FIRST_HOUR] is None:
                timetable[day][FIRST_HOUR] = f"{code} ({faculty})"
                faculty_busy.add((day, FIRST_HOUR, faculty))
                sub["hours"] -= 1
                break

    # -------------------------------------------------
    # STEP 2: Allocate remaining hours (NO CONSECUTIVE)
    # -------------------------------------------------
    for code, sub in theory_subjects:
        remaining_hours = sub["hours"]
        faculty = sub["faculty"]

        for day in DAYS:
            if remaining_hours == 0:
                break

            slots = list(TIME_SLOTS)

            for i, slot in enumerate(slots):
                if remaining_hours == 0:
                    break

                if slot in BREAK_SLOTS or slot == FIRST_HOUR:
                    continue

                if timetable[day][slot] is not None:
                    continue

                # ---------- CHECK PREVIOUS SLOT ----------
                if i > 0:
                    prev_slot = slots[i - 1]
                    prev_value = timetable[day][prev_slot]

                    if prev_value:
                        # Same subject check
                        if prev_value.startswith(code):
                            continue

                        # Same faculty check
                        if f"({faculty})" in prev_value:
                            continue

                # ---------- FACULTY AVAILABILITY ----------
                if (day, slot, faculty) in faculty_busy:
                    continue

                # ---------- PLACE THEORY ----------
                timetable[day][slot] = f"{code} ({faculty})"
                faculty_busy.add((day, slot, faculty))
                remaining_hours -= 1
