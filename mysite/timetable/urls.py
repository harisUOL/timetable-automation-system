from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('class/<int:class_group_id>/', views.index, name='class_timetable'),
    path(
    'assign/<int:class_group_id>/<str:day>/<int:period>/',
    views.assign_teacher,
    name="assign_teacher"),
]