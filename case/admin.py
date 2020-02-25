from django.contrib import admin

# Register your models here.
from .models import Case

class CaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'hearing_date' ,'case_status']


admin.site.register(Case, CaseAdmin)
