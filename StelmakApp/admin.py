from django.contrib import admin
from StelmakApp.models import Educational_ProgrammModel
admin.site.register (Educational_ProgrammModel)

class EducationalProgramAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_of_birth',
        'year',
        'courses',
        'last_year',
        'result',
        'current_date',
    )

    list_filter = ('year', 'courses', 'last_year')

    search_fields = ('name',)

    ordering = ('-current_date',)