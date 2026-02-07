class Timetable:
    def __init__(self):
        self.slots = {}  # {(day, period, class_id): (teacher_id, subject)}
