from django.contrib import admin
from django.db import transaction
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
    actions = ["duplicate_teachers"]   # 👈 Add this

    @admin.action(description="Duplicate selected teachers")
    def duplicate_teachers(self, request, queryset):
        for teacher in queryset:
            with transaction.atomic():

                # Create duplicate teacher
                new_teacher = Teacher.objects.create(
                    name=f"{teacher.name} (Copy)",
                    is_active=teacher.is_active,
                    is_cover_teacher=teacher.is_cover_teacher,
                )

                # Duplicate subjects
                teacher_subjects = TeacherSubject.objects.filter(
                    teacher=teacher
                )

                for ts in teacher_subjects:
                    TeacherSubject.objects.create(
                        teacher=new_teacher,
                        subject=ts.subject
                    )

                # Duplicate availability
                availability = TeacherAvailability.objects.filter(
                    teacher=teacher
                )

                for slot in availability:
                    TeacherAvailability.objects.create(
                        teacher=new_teacher,
                        day=slot.day,
                        period=slot.period
                    )

        self.message_user(request, "Selected teachers duplicated successfully.")


@admin.register(ClassGroup)
class ClassGroupAdmin(admin.ModelAdmin):
    list_display = ("grade", "section")
    inlines = [SubjectRequirementInline]
    actions = ["duplicate_class_groups"]   # 👈 Add this line

    @admin.action(description="Duplicate selected class groups")
    def duplicate_class_groups(self, request, queryset):
        for class_group in queryset:
            with transaction.atomic():
                new_class_group = ClassGroup.objects.create(
                    grade=class_group.grade,
                    section=class_group.section
                )

                requirements = SubjectRequirement.objects.filter(
                    class_group=class_group
                )

                for req in requirements:
                    SubjectRequirement.objects.create(
                        class_group=new_class_group,
                        subject=req.subject,
                        periods_per_week=req.periods_per_week
                    )

        self.message_user(request, "Selected class groups duplicated successfully.")


admin.site.register(Grade)
admin.site.register(Section)
admin.site.register(Subject)
