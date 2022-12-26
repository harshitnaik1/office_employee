from django.contrib import admin

from home.models import Department, Employee, Role

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Role)