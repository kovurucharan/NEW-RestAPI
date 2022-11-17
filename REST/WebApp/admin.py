from django.contrib import admin

# Register your models here.
from WebApp.models import Employees
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['EmpId','FirstName','LastName']
admin.site.register(Employees,EmployeeAdmin)
