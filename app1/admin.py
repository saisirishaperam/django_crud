from django.contrib import admin

# Register your models here.
from app1.models import employe

class emp_admin(admin.ModelAdmin):
    list_display = ['name','id_no','email']

admin.site.register(employe, emp_admin)