from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    que_display = ('id','name','code','description','is_Published','q_date')
    que_display_links = ('id','name')
    que_editable = ('is_Published',)
    search_fields = ('name','code')
    que_per_page = 25

admin.site.register(Question, QuestionAdmin)