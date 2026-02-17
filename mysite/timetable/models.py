from django.db import models

class Grade(models.Model):
    name = models.CharField(max_length=20)  # e.g., 10, 11, 12

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=10)  # A, B, C

    def __str__(self):
        return self.name


class ClassGroup(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade.name}{self.section.name}"


# ===============================
# Subjects
# ===============================

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ===============================
# Teachers
# ===============================

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_cover_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher} - {self.subject}"


# ===============================
# Availability
# ===============================

DAYS_OF_WEEK = [
    ("MON", "Monday"),
    ("TUE", "Tuesday"),
    ("WED", "Wednesday"),
    ("THU", "Thursday"),
    ("FRI", "Friday"),
    ("SAT", "Saturday"),
]

class TeacherAvailability(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    period = models.IntegerField()

    def __str__(self):
        return f"{self.teacher} - {self.day} - Period {self.period}"


# ===============================
# Subject Requirements per Class
# ===============================

class SubjectRequirement(models.Model):
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    periods_per_week = models.IntegerField()

    def __str__(self):
        return f"{self.class_group} - {self.subject}"