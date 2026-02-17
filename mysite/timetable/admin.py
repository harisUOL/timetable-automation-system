from django.contrib import admin
from .models import *

# ===============================
# Inline configurations
# ===============================

class TeacherSubjectInline(admin.TabularInline):
    model = TeacherSubject
    extra = 1


class TeacherAvailabilityInline(admin.TabularInline):
    model = TeacherAvailability
    extra = 1


class SubjectRequirementInline(admin.TabularInline):
    model = SubjectRequirement
    extra = 1


# ===============================
# Admin Configurations
# ===============================

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "is_cover_teacher")
    list_filter = ("is_active", "is_cover_teacher")
    inlines = [TeacherSubjectInline, TeacherAvailabilityInline]


@admin.register(ClassGroup)
class ClassGroupAdmin(admin.ModelAdmin):
    list_display = ("grade", "section")
    inlines = [SubjectRequirementInline]


admin.site.register(Grade)
admin.site.register(Section)
admin.site.register(Subject)