from django.shortcuts import redirect, get_object_or_404, render
from .models import (
    ClassGroup,
    TimetableEntry,
    Teacher,
    Subject,
    TeacherAvailability
)


def index(request, class_group_id=None):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT"]
    periods = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    class_groups = ClassGroup.objects.all()

    selected_class = None
    timetable = {}

    if class_group_id:
        selected_class = get_object_or_404(ClassGroup, id=class_group_id)

        entries = TimetableEntry.objects.filter(
            class_group=selected_class
        )

        for entry in entries:
            timetable.setdefault(entry.day, {})
            timetable[entry.day][entry.period] = entry

    return render(request, "timetable/index.html", {
        "days": days,
        "periods": periods,
        "timetable": timetable,
        "class_groups": class_groups,
        "selected_class": selected_class
    })


def assign_teacher(request, class_group_id, day, period):
    class_group = get_object_or_404(ClassGroup, id=class_group_id)
    teachers = Teacher.objects.filter(is_active=True)
    subjects = Subject.objects.all()

    teacher_data = []

    for teacher in teachers:
        total_available = TeacherAvailability.objects.filter(
            teacher=teacher
        ).count()

        total_assigned = TimetableEntry.objects.filter(
            teacher=teacher
        ).count()

        remaining = max(total_available - total_assigned, 0)

        teacher_data.append({
            "teacher": teacher,
            "assigned": total_assigned,
            "remaining": remaining
        })

    if request.method == "POST":
        teacher_id = request.POST.get("teacher")
        subject_id = request.POST.get("subject")

        if not teacher_id or not subject_id:
            return render(request, "timetable/assign.html", {
                "class_group": class_group,
                "day": day,
                "period": period,
                "teachers": teacher_data,
                "subjects": subjects,
                "error": "Please select both teacher and subject."
            })

        teacher = get_object_or_404(Teacher, id=teacher_id)
        subject = get_object_or_404(Subject, id=subject_id)

        # ✅ Availability check
        if not TeacherAvailability.objects.filter(
            teacher=teacher,
            day=day,
            period=period
        ).exists():
            return render(request, "timetable/assign.html", {
                "class_group": class_group,
                "day": day,
                "period": period,
                "teachers": teacher_data,
                "subjects": subjects,
                "error": "Teacher not available at this time."
            })


        # ✅ Clash check
        if TimetableEntry.objects.filter(
            teacher=teacher,
            day=day,
            period=period
        ).exists():
            return render(request, "timetable/assign.html", {
                "class_group": class_group,
                "day": day,
                "period": period,
                "teachers": teacher_data,
                "subjects": subjects,
                "error": "Teacher already assigned elsewhere."
            })

        # ⭐ ADD THIS HERE ⭐
        # Remove existing entry for this class/day/period
        TimetableEntry.objects.filter(
            class_group=class_group,
            day=day,
            period=period
        ).delete()

        # Now create new one
        TimetableEntry.objects.create(
            class_group=class_group,
            day=day,
            period=period,
            teacher=teacher,
            subject=subject
        )

        return redirect("class_timetable", class_group_id=class_group.id)


    return render(request, "timetable/assign.html", {
        "class_group": class_group,
        "day": day,
        "period": period,
        "teachers": teacher_data,
        "subjects": subjects
    })
