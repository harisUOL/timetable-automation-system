from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT"]

    # Periods including recess placeholder
    periods = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Empty timetable for now
    timetable = {}

    return render(request, "timetable/index.html", {
        "days": days,
        "periods": periods,
        "timetable": timetable
    })