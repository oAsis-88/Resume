from django.contrib import admin
from .models import ProgrammingLanguages


class ProgramLangAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'process')
    list_display_links = ('title', 'content', 'process',)
    search_fields = ('title', 'content', 'process',)


admin.site.register(ProgrammingLanguages, ProgramLangAdmin)
