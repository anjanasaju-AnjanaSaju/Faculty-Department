from django.contrib import admin
from .models import FacDepartment

class FacDepartmentAdmin(admin.ModelAdmin):
    search_fields=('IT','Mechanical','Electrical','Teachers')
admin.site.register(FacDepartment,FacDepartmentAdmin)
