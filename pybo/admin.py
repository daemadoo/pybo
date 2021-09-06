from django.contrib import admin
from pybo.models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
