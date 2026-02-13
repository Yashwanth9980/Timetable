from services.data_manager import load
from config.constants import DAYS, TIME_SLOTS, BREAK_SLOTS, FIRST_HOUR

def allocate_labs(timetable):
    """
    Allocates lab subjects with the following constraints:
    - Only ONE lab per day
    - Each lab occupies TWO CONTINUOUS hours
    - No lab in FIRST HOUR
    - No lab during breaks
    - No overlapping labs
    """

    subjects = load("subjects.json")

    # Collect only lab subjects
    lab_subjects = [
        (code, sub) for code, sub in subjects.items()
        if sub.get("type") == "lab"
    ]

    lab_days_used = set()      # Days that already have a lab
    lab_slots_used = set()     # (day, slot) used by labs

    for code, sub in lab_subjects:
        placed = False

        for day in DAYS:
            # ❌ Rule: only one lab per day
            if day in lab_days_used:
                continue

            slots = list(TIME_SLOTS)

            for i in range(len(slots) - 1):
                s1 = slots[i]
                s2 = slots[i + 1]

                # ❌ Skip breaks
                if s1 in BREAK_SLOTS or s2 in BREAK_SLOTS:
                    continue

                # ❌ No lab in first hour
                if s1 == FIRST_HOUR:
                    continue

                # ❌ Avoid overlapping lab slots
                if (day, s1) in lab_slots_used or (day, s2) in lab_slots_used:
                    continue

                # ✅ Place lab if both slots are empty
                if timetable[day][s1] is None and timetable[day][s2] is None:
                    timetable[day][s1] = f"{code} (Lab)"
                    timetable[day][s2] = f"{code} (Lab)"

                    lab_days_used.add(day)
                    lab_slots_used.add((day, s1))
                    lab_slots_used.add((day, s2))

                    placed = True
                    break

            if placed:
                break
