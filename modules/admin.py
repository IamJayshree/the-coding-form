from django.contrib import admin
from .models import Module

class ModuleAdmin(admin.ModelAdmin):
    mod_display = ('id','titlename','description','qcode','is_Published','mod_date')
    mod_display_links = ('id','titlename')
    mod_filter = ('qcode',)
    mod_editable = ('is_Published',)
    search_fields = ('titlename','qcode')
    mod_per_page = 25

admin.site.register(Module, ModuleAdmin)