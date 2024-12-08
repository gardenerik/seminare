from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Enrollment, School, User

admin.site.register(User, UserAdmin)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["user", "school", "grade", "category"]
    list_filter = ["school", "grade", "category"]


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    search_fields = ["name", "edu_id", "address"]
    list_display = ["name", "short_name", "edu_id", "address"]