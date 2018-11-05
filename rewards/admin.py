from django.contrib import admin
from .models import Employee

# class EmployeeAdmin(admin.ModelAdmin):
#     fields = ['name', 'points_remain', 'points_received']

admin.site.register(Employee)
