from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Caregiver, Student


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_auth', ]
    empty_value_display = 'unknown'


@admin.register(Caregiver)
class CaregiverAdmin(admin.ModelAdmin):
    model = Caregiver
    list_display = ['user', 'first_name', 'last_name', 'email']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email', 'total_points']
