from config.constants import TIME_SLOTS

def display(timetable):
    print("\nDYNAMIC COLLEGE TIMETABLE\n")
    print("DAY".ljust(6), end="")
    for slot in TIME_SLOTS:
        print(slot.center(18), end="")
    print()

    for day in timetable:
        print(day.ljust(6), end="")
        for slot in TIME_SLOTS:
            print((timetable[day][slot] or "-").center(18), end="")
        print()
