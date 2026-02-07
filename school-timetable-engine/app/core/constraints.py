def teacher_is_available(teacher, day, period):
    return period in teacher.availability.get(day, [])

def teacher_can_teach(teacher, subject):
    return subject in teacher.subjects
